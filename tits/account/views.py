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