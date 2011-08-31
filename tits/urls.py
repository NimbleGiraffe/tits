from django.conf.urls.defaults import patterns, include, url
from django.contrib import admin
import settings

admin.autodiscover()
# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
     url(r'^admin/', include(admin.site.urls)),
     
     url(r'^$', 'nips.views.index'),
     url(r'^account/', include('account.urls')),
     url(r'^nipple/', include('nips.urls')),
     url(r'^search/', include('haystack.urls')),
)

if settings.USER != 'wbstueck':
    urlpatterns += patterns('',
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root' : settings.MEDIA_ROOT}),
    )