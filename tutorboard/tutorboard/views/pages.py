from django.shortcuts import render
from django.forms.models import modelformset_factory
from django.template import RequestContext

from tutorboard.models import Tutor
from tutorboard.forms import AvailabilityForm
from tutorboard.filters import TutorFilter

def page_tutor_list(request):
    template_name = 'tutorboard/tutor_list.html'
    filter =  TutorFilter(request.GET)
    context = RequestContext(request, {'filter': filter})
    return render(request, template_name, context)

def page_tutor_availability(request):
    template_name = 'tutorboard/tutor_availability.html'
    TutorFormSet = modelformset_factory(Tutor, form=AvailabilityForm)
    if request.method == 'POST':
        formset = TutorFormSet(request.POST, request.FILES)
        if formset.is_valid():
            formset.save()
    else:
        formset = TutorFormSet()

    context = RequestContext(request, {'formset': formset})
    return render(request, template_name, context)
