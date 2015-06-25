# tutorboard/urls.py

from django.conf.urls import patterns, url

from tutorboard.views import tutor, capability, pages

urlpatterns = patterns("",

    ################
    #     Pages
    ################

    # /tutorboard/
    url(
       regex=r"^$",
       view=pages.page_tutor_list,
       name='home'
    ),

    # /tutorboard/availability
    url(
       regex=r'^availability/$',
       view=pages.page_tutor_availability,
       name='availability'
    ),

    #########################
    #     Tutor Views
    #########################

    url(
       regex=r"^list/page(?P<page>[0-9]+)/$",
       view=tutor.TutorView.as_view(),
       name='list'
    ),

    # Create: /tutorboard/create
    url(
       regex=r"^create/",
       view=tutor.TutorCreate.as_view(),
       name='create'
    ),

    # Update: /tutorboard/{tutorID}/
    url(
       regex=r'^(?P<tutor_id>\d+)/$',
       # view = views.update_tutor,
       view=tutor.TutorUpdateView.as_view(),
       name='update'
    ),

    ##############################
    # Capability/Subject Views
    ##############################

    # Create capability page
    # /tutorboard/capability/create
    url(
       regex=r"^capability/create/",
       view=capability.CapabilityCreate.as_view(),
       name='capability_create'
    ),

    # Delete capability page
    # /tutorboard/capability/{tutorID}/delete/
    url(
       regex=r'^capability/(?P<capability_id>\d+)/delete/$',
       view=capability.CapabilityDelete.as_view(),
       name='capability_delete'
    ),

    # Edit capability page
    # /tutorboard/capability/{tutorID}/
    url(
       regex=r'^capability/(?P<capability_id>\d+)/$',
       view=capability.CapabilityUpdateView.as_view(),
       name='capability_update'
    ),


)
