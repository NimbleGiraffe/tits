from django.contrib.auth.models import User
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from nips.models import Nipple, NippleOpinion
from django.core.exceptions import ObjectDoesNotExist
from operator import attrgetter

@login_required
def index(request):
    request.session.set_expiry(299)
    nip_dict = {}
    nips = Nipple.objects.all()
    for i in nips:
        if i.votes > 0:
            nip_dict[i] = float(i.score)/i.votes
        else:
            nip_dict[i] = 0.0
    print nip_dict
    print sorted(nip_dict, key=attrgetter("-score"))
    print nip_dict
    return render_to_response("nips/index.html", {'nip_dict':nip_dict}, context_instance=RequestContext(request))

@login_required
def day_four(request):
    request.session.set_expiry(299)
    dfn = DayFourNipple.objects.all()
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