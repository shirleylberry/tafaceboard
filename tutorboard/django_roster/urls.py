from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib.auth.views import login, logout
from django.views.generic.base import RedirectView
from django.conf import settings
from django.conf.urls.static import static
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:

    url(r'^', include('tutorboard.urls')),
    #url(r'^$', RedirectView.as_view(url='/tutorboard/')),
    #url(r'^tutorboard/', include('tutorboard.urls')),
    url(r'^search/', include('haystack.urls')),
    url(r'^login/$', login),
    url(r'^logout/$', logout),
    

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),


    url(r'^admin/', include(admin.site.urls)),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


