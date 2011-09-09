from django.conf.urls.defaults import *
from django.views.generic.simple import redirect_to
from django.views.generic.simple import direct_to_template

urlpatterns = patterns('',
    url(r'^(?P<nipple_id>\d+)/$', "nips.views.nipple"),
    url(r'^dayfour/$', "nips.views.day_four"),
)
