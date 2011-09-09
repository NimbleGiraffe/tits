from django.contrib.auth.models import User
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from nips.models import Nipple, NippleOpinion, DayFour
from django.core.exceptions import ObjectDoesNotExist
from operator import attrgetter

@login_required
def index(request):
    request.session.set_expiry(299)
    nips = []
    n = Nipple.objects.all()
    dfn = [x.nipple for x in DayFour.objects.all()]
    for i in dfn:
        nips.append(i)
    return render_to_response("nips/index.html", {'nips':nips}, context_instance=RequestContext(request))

@login_required
def day_four(request):
    request.session.set_expiry(299)
    dfn = DayFour.objects.all()
    nips = [x.nipple for i in dfn]
    return render_to_response("nips/dayfour.html", {'nips':nips}, context_instance=RequestContext(request))


@login_required
def nipple(request, nipple_id):
    request.session.set_expiry(299)
    nipple = Nipple.objects.get(id=int(nipple_id))
    if request.method =="POST":
        if 'delete' in request.POST:
            no = NippleOpinion.objects.get(user=request.user, nipple=nipple)
            val = no.score
            no.delete()
            nipple.score -= val
            nipple.votes -= 1
            nipple.save()
            return HttpResponseRedirect("/nipple/"+str(nipple_id)+"/")
        else:
            val = int(request.POST['score'])
            if 'comment' in request.POST:
                comment = request.POST['comment']
            else:
                return HttpResponseRedirect("/account/logout/")
            no = NippleOpinion(user=request.user, nipple=nipple, score=val, comment=comment)
            no.save()
            nipple.score += val
            nipple.votes += 1
            nipple.save()
            return HttpResponseRedirect("/nipple/"+str(nipple_id)+"/")
        
    if nipple.votes > 0:
        avg_score = float(nipple.score)/nipple.votes
    else:
        avg_score = 0.0
    opinions = NippleOpinion.objects.filter(nipple=nipple)
    
    try:
        user_opinion = NippleOpinion.objects.get(user=request.user, nipple=nipple)
        voted = True
    except ObjectDoesNotExist:
        user_opinion = None
        voted = False
        
    lazy_fucks = []
    for i in User.objects.all():
        if i not in [o.user for o in opinions]:
            lazy_fucks.append(i)
    
    return render_to_response("nips/nipple.html", {'nipple':nipple, 'opinions':opinions, 'lazy_fucks':lazy_fucks, 'voted':voted, 'user_opinion':user_opinion, 'avg_score':avg_score, 'user':request.user}, context_instance=RequestContext(request))
