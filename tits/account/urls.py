from django.conf.urls.defaults import *
from django.views.generic.simple import redirect_to
from django.views.generic.simple import direct_to_template

urlpatterns = patterns('',
    url(r'^login/$', "account.views.login_user", name='login_user'),
    url(r'^logout/$', 'django.contrib.auth.views.logout', {'next_page' : '/'}, name='logout'),
    url(r'^change_password/$', "account.views.change_password"),
    )