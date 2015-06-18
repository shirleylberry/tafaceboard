# tutorboard/urls.py

from django.conf.urls import patterns, url

from tutorboard import views

urlpatterns = patterns("",

    # /tutorboard/
    url(
       regex=r"^$",
       view=views.TutorView.as_view(),
       name='list'
    ),

    # /tutorboard/hidden
    url(
       regex=r"hidden/$",
       view=views.AllTutorView.as_view(),
       name='hidden'
    ),

    # Create tutor page
    # /tutorboard/create
    url(
       regex=r"^create/",
       view=views.TutorCreate.as_view(),
       name='create'
    ),

    # Edit tutor page
    # /tutorboard/{tutorID}/
    url(
       regex=r'(?P<tutor_id>\d+)/$',
       # view = views.update_tutor,
       view=views.TutorUpdateView.as_view(),
       name='update'
    ),

    # /tutorboard/availability
    url(
       regex=r'^availability/$',
       view=views.tutor_availability,
       name='availability'
    ),

    # Get returns a checkbox list of subjects. Post updates the capability for one tutor and one subject
    url(
       regex=r'^(?P<tutor_id>\d+)/update/ajax/subjectlist/$',
       view=views.SubjectListAjax.as_view(),
       name='ajaxSubjectList'
    ),

)
