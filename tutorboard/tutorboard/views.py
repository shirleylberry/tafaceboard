# tutorboard/views.py

from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned
from django.views.generic import ListView, CreateView, UpdateView
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, render_to_response
from django.forms.models import modelformset_factory
from django.template.loader import render_to_string
from django.template import RequestContext, loader
from django.core.context_processors import csrf
from django.views.generic.base import View
from django.db.models import Q

from tutorboard.models import Tutor, Capability, Subject, SubjectUpdate, LEVEL, GENDER, AREA, HIREDFOR, PROFDEV
from .forms import SearchForm, TutorForm, CapabilityForm, AvailabilityForm, SubjectForm

# downloaded from djangosnippets.com[942]
from snippets import render_block_to_string


class TutorView(View):
    tutor_list = []
    template_name = "tutorboard/tutor_list.html"

    def get(self, request, *args, **kwargs):
        tutor_list = Tutor.objects.prefetch_related(
            'capability_set__subject').all().exclude(hidden=True)

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
				                   Q(capability__notes__icontains=search))

        tutors = tutors.distinct()
        tutors.prefetch_related(
            'capability_set__subject',)

        context = RequestContext (request, {'tutor_list': tutors})
        return render(request, self.template_name, context)


class AllTutorView(TutorView):  #include hidden tutors
    def get(self, request, *args, **kwargs):
        tutor_list = Tutor.objects.prefetch_related(
            'capability_set__subject',).all()


        searchForm = SearchForm()

        context = RequestContext (request, {'tutor_list' : tutor_list,
                                  'search_form':searchForm})
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
    model = Tutor
    template_name = "tutorboard/tutor_create.html"
    success_url = ".."
    form_class = TutorForm

def update_tutor(request, tutor_id):
    #if tutor_id == '0':
    #    TutorFormSet = modelformset_factory(Tutor, form=TutorForm, extra=1, can_delete=True)
    #else:
    #    TutorFormSet = modelformset_factory(Tutor, form=TutorForm, extra=0, can_delete=True)


    # if tutor_id is 0, then we are updating or creating a new tutor
    # we can avoid a lot of database calls in this case

    if tutor_id == 0 or tutor_id == '0':
        current_tutor = None
        nextTutor = None
        prevTutor = None
    else:
        # Get all tutors to minimize database requests.s
        # We will find the current tutor, previous tutor, and next tutor later
        tutor_queryset = Tutor.objects.all()
        tutor_list = list(tutor_queryset)
        current_tutor = tutor_queryset.get(pk=tutor_id)

        nextTutor = findNextTutor(tutor_id, tutor_list)
        prevTutor = findPrevTutor(tutor_id, tutor_list)

    if request.method == 'POST':
        # form is being submitted
        tutor_form = TutorForm(request.POST, request.FILES, instance = current_tutor)

        # Check if the form is valid
        if  tutor_form.is_valid():

            # in case current_tutor is None (if we making a new tutor) 
            # then get the instance from the form
            tutor_to_save = tutor_form.save(commit = False)
            tutor_to_save = tutor_form.save()
            tutor_form.save_m2m()
            print("Tutor to save id: " + str(tutor_to_save.id))
            # Check which save button was pressed.
            # If Save and Next was clicked, respond with the next tutor
            redirectToTutor = None
            if 'save' in request.POST:
                #redirectToTutor = str(tutor_to_save.id)
                success= "Tutor Saved"
                return HttpResponseRedirect('/tutorboard/')
            elif 'saveAndNext' in request.POST:
                redirectToTutor = str(nextTutor.id)
            else:
                redirectToTutor = '0'


            success= "Tutor Saved"
            return HttpResponseRedirect('/tutorboard/' + redirectToTutor + '/update/')
        else:
            print("Form Invalid.  Tutor not saved.")
            form_errors = tutor_form.errors
            print form_errors
            return render_to_response ('tutorboard/tutor_update.html', {
                                  'tutor_form' : tutor_form,
             #                     'capability_formset': capability_formset,
                                  'tutor_id': tutor_id,
                                  'next_tutor': nextTutor,
                                  'prev_tutor': prevTutor,
     #                             'subject_list': subject_list,
                                  'form_errors': form_errors},
                      context_instance=RequestContext(request))

    else:

        if current_tutor == None:
            tutor_form = TutorForm()
        else:
            tutor_form = TutorForm(instance=current_tutor)


        return render_to_response('tutorboard/tutor_update.html', {
                                  'tutor_form' : tutor_form,
 #                                 'capability_formset': capability_formset,
                                  'tutor_id': tutor_id,
                                  'next_tutor': nextTutor,
                                  'prev_tutor': prevTutor,
      #                            'subject_list': subject_list},
                                    },
                                  context_instance=RequestContext(request))

def tutor_availability(request):
    template_name = 'tutorboard/tutor_availability.html'
    TutorFormSet = modelformset_factory(Tutor, form=AvailabilityForm)
    if request.method == 'POST':
        formset = TutorFormSet(request.POST, request.FILES)
        if formset.is_valid():
            formset.save()
    else:
        formset = TutorFormSet()

    context = RequestContext (request, {'formset':formset})
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

        capability_list = list(Capability.objects.all().filter(tutor__id = tutor_id))


        for sub in subject_list:
            subUpdate = SubjectUpdate()
            subUpdate.tutor_id = tutor_id
            subUpdate.subject = sub

            try:

                # Make a subject form for this subject
                subForm = SubjectForm(instance = sub)
                subUpdate.subject_form = subForm

                cap = None
                for capability in capability_list:
                    if capability.subject.id == sub.id:
                        cap = capability

                subUpdate.capability = cap

                    # Make a capability form for the found capability
                capForm = CapabilityForm(instance = cap)
                subUpdate.capability_form = capForm

                model.append(subUpdate)
            except MultipleObjectsReturned:
                print("Multiple capabilities found for the same subject and tutor. Delete one of the capabilities.")

        context = RequestContext (request, {
            'model':model,
            'tutor_id':tutor_id,
            })
        return render(request, self.template_name, context)


    def post(self, request, *args, **kwargs):

        if request.is_ajax() == False:
            return "Request is not ajax"
        else:

            # Available Data
            tutor_id = self.kwargs['tutor_id']                      # From URL
            checkedOrUnchecked = request.POST.get('checked', '')    # These may not exist, check carefully
            subject_id = request.POST.get('subjectID', None)
            if subject_id == -1:subject_id = None
            capability_id = request.POST.get('capabilityID', None)
            if capability_id == -1: capability_id = None

            json_result = 'request is ajax'

            if checkedOrUnchecked == 'checked':

                cap = Capability.objects.create(subject_id=subject_id, tutor_id=tutor_id)
                sub_for_cap = cap.subject

                subUpdate = SubjectUpdate()
                subUpdate.tutor_id = tutor_id
                subUpdate.subject = sub_for_cap
                subForm = SubjectForm(instance = sub_for_cap)
                subUpdate.subject_form = subForm

                subUpdate.capability = cap

                capForm = CapabilityForm(instance = cap)
                subUpdate.capability_form = capForm

                model = []
                model.append(subUpdate)

                context = RequestContext (request, {
                    'model':model,
                    'tutor_id':tutor_id,
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

                context = RequestContext (request, {
                    'model':model,
                    'tutor_id':tutor_id,
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
                    capForm = CapabilityForm(request.POST, instance = cap)
                    print("Capability updated")
                    json_result = "<span style=\"color:green;\">Subject updated.</span>"
                except ObjectDoesNotExist:
                    capForm = CapabilityForm(request.POST)
                    print("New capability created")
                    json_result = "<span style=\"color:green;\">New subject added to tutor</span>"



                # If the form is valid, save it
                if capForm.is_valid():
                    cap = capForm.save(commit=False)
                    #sub = cap.subject # We have the option of getting the subject from the cap if the DB is slow
                    cap.save()
                    # Call highestLevel function
                    tutor = Tutor.objects.get(id=tutor_id)
                    tutor.highestLevel = getHighestLevel(tutor_id)
                    tutor.save()
                else :
                    print("Form Fails")
                    json_result = "<span style=\"color:red;\">Update failed</span>"

                # Return form and model to template
                subUpdate = SubjectUpdate()
                subUpdate.capability = cap
                subUpdate.capability_form = capForm
                subUpdate.subject = sub

                model = []
                model.append(subUpdate)

                context = RequestContext (request, {
                    'model':model,
                    'tutor_id':tutor_id,
                    'json_result': json_result,
                    })
                return render(request, self.template_name, context)



            return HttpResponse(simplejson.dumps(json_result),mimetype='application/json')


# View helpers. These do not return http responses

def findNextTutor(tutor_id, tutor_list):

    # tutor_id was the number in the URL

    for index, tutor in enumerate(tutor_list): # we just want to find the index of the tutor
    # find the current tutor in the list, make sure its not the last tutor in the list
        if int(tutor.id) == int(tutor_id) and index+1 < len(tutor_list):
            return tutor_list[index+1:index+2][0] # returns the tutor object
    return None

def findPrevTutor(tutor_id, tutor_list):
    # tutor_id was the number in the URL

    for index, tutor in enumerate(tutor_list): # we just want to find the index of the tutor

    # find the current tutor in the list, make sure its no the last tutor in the list
        if int(tutor.id) == int(tutor_id) and index+1 > 1:
            return tutor_list[index-1:index][0]
    return None

def getHighestLevel(tutor_id):
    all_caps = Capability.objects.all().filter(tutor__id = tutor_id)
    highestlevel = "Professional"
    for cap in all_caps:
        if cap.level == "director":
            return "Director"
        elif cap.level == "expert":
            highestlevel = "Expert"
    return highestlevel
