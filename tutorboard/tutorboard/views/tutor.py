from django.views.generic import CreateView, UpdateView
from django.views.generic import ListView
from django.core.urlresolvers import reverse
from django.core.exceptions import ObjectDoesNotExist
from tutorboard.models import Tutor, Subject
from tutorboard.forms import TutorForm, CapabilityForm
from tutorboard.filters import TutorFilter
from tutorboard.views.helpers import findNextTutor, findPrevTutor

class TutorView(ListView):
    tutor_list = []
    model = Tutor
    context_object_name = 'tutor_list'
    template_name = 'tutorboard/partials/tutorboard.html'
    paginate_by = 10

    def get_queryset(self):
        qs = super(TutorView, self).get_queryset()
        print qs.count()

        # Filter
        f = TutorFilter(self.request.GET, queryset=qs)
        qs = f.qs
        print qs.count()

        # Get subjects
        qs = qs.prefetch_related('capability_set__subject',).all().exclude(hidden=True)

        # Sort
        sort_type = self.request.GET.get('sort')
        if sort_type == 'level':
            pass # TODO
        elif sort_type == 'magic':
            pass # TODO
        elif sort_type is not None:
            qs = qs.order_by(sort_type)

        print qs.count()

        return qs

    def get_context_data(self, **kwargs):
        context = super(TutorView, self).get_context_data(**kwargs)
        return context

class TutorCreate(CreateView):
    template_name_suffix = '_create'
    model = Tutor
    form_class = TutorForm
    context_object_name = 'tutor'

    def get_success_url(self):
        return reverse('update', args=(self.object.id,))

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
            valid_cap = True
            try:
                sub_test = cap.subject
            except ObjectDoesNotExist:
                valid_cap = False
                cap.save()
                cap.delete()

            cap_form = CapabilityForm(instance=cap, auto_id='')
            capability_forms.append(cap_form)
            if valid_cap:
                for sub in subjects:
                    if cap.subject and sub == cap.subject:
                        sub.selected = True

        context['capability_forms'] = capability_forms
        return context
