# tutorboard/views.py

from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned
from django.views.generic import CreateView, UpdateView, DeleteView
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, render_to_response
from django.forms.models import modelformset_factory
from django.forms.formsets import formset_factory
from django.template import RequestContext
from django.views.generic.base import View
from django.db.models import Q
from django.core.urlresolvers import reverse

from tutorboard.models import Tutor, Capability, Subject, SubjectUpdate, LEVEL, GENDER, AREA, HIREDFOR, PROFDEV
from .forms import SearchForm, TutorForm, CapabilityForm, AvailabilityForm, SubjectForm, CapabilityFormSet


class TutorView(View):
    tutor_list = []
    template_name = "tutorboard/tutor_list.html"

    def get(self, request, *args, **kwargs):
        tutor_list = Tutor.objects.prefetch_related(
            'capability_set__subject',
            ).all().exclude(hidden=True)

        context = RequestContext(request, {
            'tutor_list': tutor_list,
        })

        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        self.template_name = "tutorboard/partials/tutorboard.html"
        search = request.POST.get('search')
        tutors = Tutor.objects.all()

        # This might be horrifically slow
        print search
        if search:
            tutors = tutors.filter(Q(lname__icontains=search) |
                                   Q(fname__icontains=search) |
                                   Q(gotofor__icontains=search) |
                                   Q(neighborhood__icontains=search) |
                                   Q(bioline1__icontains=search) |
                                   Q(bioline2__icontains=search) |
                                   Q(bioline3__icontains=search) |
                                   Q(bioline4__icontains=search) |
                                   Q(bioline5__icontains=search) |
                                   Q(availability_note__icontains=search) |
                                   Q(capability__subject__name__icontains=search) |
                                   Q(capability__notes__icontains=search)
                                   )

        tutors = tutors.distinct()
        tutors.prefetch_related(
            'capability_set__subject',)

        context = RequestContext(request, {'tutor_list': tutors})
        return render(request, self.template_name, context)

class AllTutorView(TutorView):  # include hidden tutors
    def get(self, request, *args, **kwargs):
        tutor_list = Tutor.objects.prefetch_related(
            'capability_set__subject',).all()


        searchForm = SearchForm()

        context = RequestContext(request, {'tutor_list': tutor_list,
                                           'search_form': searchForm})
        return render(request, self.template_name, context)


class TutorCreate(CreateView):
    template_name_suffix = '_create'
    model = Tutor
    form_class = TutorForm
    context_object_name = 'tutor'

    def get_success_url(self):
        return reverse('update',args=(self.object.id,))

class TutorUpdateView(UpdateView):
    model = Tutor
    template_name_suffix = '_update'
    form_class = TutorForm
    pk_url_kwarg = 'tutor_id'
    context_object_name = 'tutor'

    def get_queryset(self):
        qs = super(TutorUpdateView, self).get_queryset()
        qs.prefetch_related('capability_set_subject')
        return qs

    def get_context_data(self, **kwargs):
        context = super(TutorUpdateView, self).get_context_data(**kwargs)
        tutor_list = list(Tutor.objects.all())
        nextTutor = findNextTutor(self.object.id, tutor_list)
        prevTutor = findPrevTutor(self.object.id, tutor_list)
        context['next_tutor'] = nextTutor
        context['prev_tutor'] = prevTutor

        capability_forms = []

        subjects = Subject.objects.all()
        context['all_subjects'] = subjects

        for cap in self.object.capability_set.all():
            cap_form = CapabilityForm(instance=cap, auto_id='')
            capability_forms.append(cap_form)
            for sub in subjects:
                if sub == cap.subject:
                    sub.selected = True
        context['capability_forms'] = capability_forms
        return context

class CapabilityUpdateView(UpdateView):
    model = Capability
    form_class = CapabilityForm
    template_name_suffix = '_update'
    pk_url_kwarg = 'capability_id'
    context_object_name = 'capability'

    def get_success_url(self):
        obj = self.get_object()
        return reverse('capability_update', kwargs={'capability_id': obj.id})

class CapabilityCreate(CreateView):
    model = Capability
    form_class = CapabilityForm
    template_name_suffix = '_update'
    #pk_url_kwarg = 'capability_id'
    context_object_name = 'capability'

    def get_success_url(self):
        return reverse('capability_update', kwargs={'capability_id': self.object.id})

    def get_form(self, form_class):
        form = super(CapabilityCreate, self).get_form(form_class)
        form.auto_id = ''
        return form

class CapabilityDelete(DeleteView):
    model = Capability
    pk_url_kwarg = 'capability_id'

    def render_to_response(self, context, **response_kwargs):
        return HttpResponse('Deleted')

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        #success_url = self.get_success_url()
        self.object.delete()
        return HttpResponse('Deleted')

def tutor_availability(request):
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

# View helpers. These do not return http responses
def findNextTutor(tutor_id, tutor_list):
    # tutor_id was the number in the URL

    for index, tutor in enumerate(tutor_list):  # we just want to find the index of the tutor
        # find the current tutor in the list, make sure its not the last tutor in the list
        if int(tutor.id) == int(tutor_id) and index + 1 < len(tutor_list):
            return tutor_list[index + 1:index + 2][0]  # returns the tutor object
    return None

def findPrevTutor(tutor_id, tutor_list):
    # tutor_id was the number in the URL

    for index, tutor in enumerate(tutor_list):  # we just want to find the index of the tutor

        # find the current tutor in the list, make sure its no the last tutor in the list
        if int(tutor.id) == int(tutor_id) and index + 1 > 1:
            return tutor_list[index - 1:index][0]
    return None

def getHighestLevel(tutor_id):
    all_caps = Capability.objects.all().filter(tutor__id=tutor_id)
    highestlevel = "Professional"
    for cap in all_caps:
        if cap.level == "director":
            return "Director"
        elif cap.level == "expert":
            highestlevel = "Expert"
    return highestlevel
