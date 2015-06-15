# tutorboard/urls.py

from django.conf.urls import patterns, url


from tutorboard import views

urlpatterns = patterns("",
    #/tutorboard/
    url(
        regex= r"^$",
	    view = views.TutorView.as_view(),
        name = 'list'
    ),
    
    #/tutorboard/hidden
    url(
        regex= r"hidden/$",
        view = views.AllTutorView.as_view(),
        name = 'hidden'
    ),

    #tutorboard/new_tutor

    url(
        regex= r"^new_tutor/",
        view = views.TutorCreate.as_view(),
        name = 'create'
    ),

    #/tutorboard/availability
    url(
        regex= r'^availability/$',
	    view = views.tutor_availability,
        name = 'availability'
    ),

    #/tutorboard/{tutorID}/update/   CLASS based
    #url(
    #    regex= r'^(?P<pk>\d+)/update/$',
    #	view = views.TutorUpdateView.as_view(),
    #    name = 'update'
    #),

    #tutorboard/{tutorID}/update/    FUNCTION based
    url(
        regex= r'(?P<tutor_id>\d+)/update/$',
    	view = views.update_tutor,
        name = 'update'
    ),
    
    # Get returns a checkbox list of subjects. Post updates the capability for one tutor and one subject
    url(
        regex= r'^(?P<tutor_id>\d+)/update/ajax/subjectlist/$',
    	view = views.SubjectListAjax.as_view(),
        name = 'ajaxSubjectList'
    ),
#ideas for urls

    # /tutors/

    # /tutorboard/tutors/{tutorID}/
    # url(r'^tutors/(?P<tutor_id>\d+)/$', views.detail, name="detail"),
 
    # /tutors/{tutorID}/edit/
    # url(r'^tutors/(?P<tutor_id>\d+)/update/$', views.update, name="update"),

    # /tutors/{tutorID}/ajax/

    # /tutors/{math or verbal}

    # /tutors/available/
)

