# tutorboard/views.py

from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned
from django.views.generic import CreateView, UpdateView
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, render_to_response
from django.forms.models import modelformset_factory
from django.template import RequestContext
from django.views.generic.base import View
from django.db.models import Q
from django.core.urlresolvers import reverse

from tutorboard.models import Tutor, Capability, Subject, SubjectUpdate, LEVEL, GENDER, AREA, HIREDFOR, PROFDEV
from .forms import SearchForm, TutorForm, CapabilityForm, AvailabilityForm, SubjectForm


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

class TutorViewWithFilterMenu(View):
    tutor_list = []
    template_name = "tutorboard/tutor_list.html"

    def get(self, request, *args, **kwargs):
        tutor_list = Tutor.objects.prefetch_related(
            'capability_set__subject',).all().exclude(hidden=True)

        subject_list = Subject.objects.all()
        area_list = ['Math', 'Verbal']
        program_list = ['Echelon', 'Cornerstone', 'Academic']
        level_list = ['Trained', 'Professional', 'Endorsed', 'Expert', 'Director']

        searchForm = SearchForm()

        context = RequestContext (request, {'tutor_list' : tutor_list,
                                  'subject_list': subject_list,
                                  'area_list': AREA,
                                  'program_list': program_list,
                                  'gender_list': GENDER,
                                  'level_list': LEVEL,
                                  'search_form':searchForm})
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

    def get_context_data(self, **kwargs):
        tutor_list = list(Tutor.objects.all())
        nextTutor = findNextTutor(self.object.id, tutor_list)
        prevTutor = findPrevTutor(self.object.id, tutor_list)
        kwargs['next_tutor'] = nextTutor
        kwargs['prev_tutor'] = prevTutor
        return super(TutorUpdateView, self).get_context_data(**kwargs)

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

class SubjectListAjax(View):
    template_name = "tutorboard/partials/subject_checkboxes.html"

    def get(self, request, *args, **kwargs):

        # Init model
        # The model will be a list of SubjectUpdate objects, start with an empty list
        model = []

        # Available data
        tutor_id = self.kwargs['tutor_id']

        # Fill out model by iterating through django models from database
        subject_list = Subject.objects.all()

        capability_list = list(Capability.objects.all().filter(tutor__id=tutor_id))

        for sub in subject_list:
            subUpdate = SubjectUpdate()
            subUpdate.tutor_id = tutor_id
            subUpdate.subject = sub

            try:

                # Make a subject form for this subject
                subForm = SubjectForm(instance=sub)
                subUpdate.subject_form = subForm

                cap = None
                for capability in capability_list:
                    if capability.subject.id == sub.id:
                        cap = capability

                subUpdate.capability = cap

                # Make a capability form for the found capability
                capForm = CapabilityForm(instance=cap)
                subUpdate.capability_form = capForm

                model.append(subUpdate)
            except MultipleObjectsReturned:
                print("Multiple capabilities found for the same subject and tutor. Delete one of the capabilities.")

        context = RequestContext(request, {
            'model': model,
            'tutor_id': tutor_id,
        })
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):

        if request.is_ajax() == False:
            return "Request is not ajax"
        else:

            # Available Data
            tutor_id = self.kwargs['tutor_id']  # From URL
            checkedOrUnchecked = request.POST.get('checked', '')  # These may not exist, check carefully
            subject_id = request.POST.get('subjectID', None)
            if subject_id == -1: subject_id = None
            capability_id = request.POST.get('capabilityID', None)
            if capability_id == -1: capability_id = None

            json_result = 'request is ajax'

            if checkedOrUnchecked == 'checked':

                cap = Capability.objects.create(subject_id=subject_id, tutor_id=tutor_id)
                sub_for_cap = cap.subject

                subUpdate = SubjectUpdate()
                subUpdate.tutor_id = tutor_id
                subUpdate.subject = sub_for_cap
                subForm = SubjectForm(instance=sub_for_cap)
                subUpdate.subject_form = subForm

                subUpdate.capability = cap

                capForm = CapabilityForm(instance=cap)
                subUpdate.capability_form = capForm

                model = []
                model.append(subUpdate)

                context = RequestContext(request, {
                    'model': model,
                    'tutor_id': tutor_id,
                })
                return render(request, self.template_name, context)

            elif checkedOrUnchecked == 'unchecked':
                # Delete the capability for tutor_id and subject_id

                sub_for_cap = None

                try:
                    capability = Capability.objects.get(id=capability_id)
                    sub_for_cap = capability.subject
                    capability.delete()

                except ObjectDoesNotExist:
                    print('Capability was deleted before it was created')

                if not sub_for_cap:
                    sub_for_cap = Subject.objects.get(id=subject_id)

                subUpdate = SubjectUpdate()

                subUpdate.subject = sub_for_cap

                subUpdate.capability = None

                model = []
                model.append(subUpdate)

                context = RequestContext(request, {
                    'model': model,
                    'tutor_id': tutor_id,
                })
                return render(request, self.template_name, context)

            else:
                # Form was posted without the checkbox
                # Save updated capability

                # Available data
                tutor_id = self.kwargs['tutor_id']


                # Subject and Capability ID were passed in with the form
                subject_id = request.POST['subject_id_manual']
                sub = Subject.objects.get(id=subject_id)
                capability_id = request.POST['capability_id_manual']
                try:
                    cap = Capability.objects.get(id=capability_id)
                    # Convert data to form using the capability we want to update
                    capForm = CapabilityForm(request.POST, instance=cap)
                    print("Capability updated")
                    json_result = "<span style=\"color:green;\">Subject updated.</span>"
                except ObjectDoesNotExist:
                    capForm = CapabilityForm(request.POST)
                    print("New capability created")
                    json_result = "<span style=\"color:green;\">New subject added to tutor</span>"



                # If the form is valid, save it
                if capForm.is_valid():
                    cap = capForm.save(commit=False)
                    # sub = cap.subject # We have the option of getting the subject from the cap if the DB is slow
                    cap.save()
                    # Call highestLevel function
                    tutor = Tutor.objects.get(id=tutor_id)
                    tutor.highestLevel = getHighestLevel(tutor_id)
                    tutor.save()
                else:
                    print("Form Fails")
                    json_result = "<span style=\"color:red;\">Update failed</span>"

                # Return form and model to template
                subUpdate = SubjectUpdate()
                subUpdate.capability = cap
                subUpdate.capability_form = capForm
                subUpdate.subject = sub

                model = []
                model.append(subUpdate)

                context = RequestContext(request, {
                    'model': model,
                    'tutor_id': tutor_id,
                    'json_result': json_result,
                })
                return render(request, self.template_name, context)

            #return HttpResponse(simplejson.dumps(json_result), mimetype='application/json')

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
