from django.contrib.auth.models import User
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from account.forms import LoginForm

def login_user(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            print "I get here"
            user = authenticate(username=User.objects.get(email=form.cleaned_data['email']).username, password=form.cleaned_data['password'])
            login(request, user)
            return HttpResponseRedirect('/')
    else:
        form = LoginForm()
    return render_to_response("account/login.html", {'form':form}, context_instance=RequestContext(request))

@login_required
def change_password(request):
    if request.method == 'POST':
        if 'old' in request.POST and 'new1' in request.POST and 'new2' in request.POST:
            if request.user.check_password(request.POST['old']):
                if len(request.POST['new1']) > 0 and len(request.POST['new2']) > 0:
                    if request.POST['new1'] == request.POST['new2']:
                        request.user.set_password(request.POST['new1'])
                        request.user.save()
                        request.session['notification'] = "Password Successfully changed."
                    else:
                        request.session['notification'] = "Passwords don't match. Learn how to type."
                else:
                    request.session['notification'] = "Set an actual password you dumb fuck."
            else:
                request.session['notification'] = "Old password is wrong."
        else:
            request.session['notification'] = 'Fill in all the fields you dumb fuck.'
    
    try:
        session_notification = request.session['notification']
        del(request.session['notification'])
    except:
        session_notification = None
    return render_to_response("account/change_password.html", {'notification':session_notification}, context_instance=RequestContext(request))