# tutorboard/urls.py

from django.conf.urls import patterns, url

from tutorboard import views

urlpatterns = patterns("",

    ################
    #     Pages
    ################

    # /tutorboard/
    url(
       regex=r"^$",
       view=views.page_tutor_list,
       name='home'
    ),

    # /tutorboard/availability
    url(
       regex=r'^availability/$',
       view=views.page_tutor_availability,
       name='availability'
    ),

    #########################
    #     Tutor Views
    #########################

    url(
       regex=r"^list/page(?P<page>[0-9]+)/$",
       view=views.TutorView.as_view(),
       name='list'
    ),

    # Create: /tutorboard/create
    url(
       regex=r"^create/",
       view=views.TutorCreate.as_view(),
       name='create'
    ),

    # Update: /tutorboard/{tutorID}/
    url(
       regex=r'^(?P<tutor_id>\d+)/$',
       # view = views.update_tutor,
       view=views.TutorUpdateView.as_view(),
       name='update'
    ),

    ##############################
    # Capability/Subject Views
    ##############################

    # Create capability page
    # /tutorboard/capability/create
    url(
       regex=r"^capability/create/",
       view=views.CapabilityCreate.as_view(),
       name='capability_create'
    ),

    # Delete capability page
    # /tutorboard/capability/{tutorID}/delete/
    url(
       regex=r'^capability/(?P<capability_id>\d+)/delete/$',
       view=views.CapabilityDelete.as_view(),
       name='capability_delete'
    ),

    # Edit capability page
    # /tutorboard/capability/{tutorID}/
    url(
       regex=r'^capability/(?P<capability_id>\d+)/$',
       view=views.CapabilityUpdateView.as_view(),
       name='capability_update'
    ),


)
