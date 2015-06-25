from django.views.generic import CreateView, UpdateView, DeleteView
from django.http import HttpResponse
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect

from tutorboard.models import Capability
from tutorboard.forms import CapabilityForm

class CapabilityUpdateView(UpdateView):
    model = Capability
    form_class = CapabilityForm
    template_name_suffix = '_update'
    pk_url_kwarg = 'capability_id'
    context_object_name = 'capability'

    def form_valid(self, form):
        context = self.get_context_data(form=form)
        context["result_message"] = "Saved."
        # This usually redirects to get_success_url, but we'll just return a template
        return self.render_to_response(context)

    def form_invalid(self, form, **kwargs):
        context = self.get_context_data(form=form)
        context['result_message'] = 'Error while saving.'
        return self.render_to_response(context)

    #def get_success_url(self):
    #    obj = self.get_object()
    #    return reverse('capability_update', kwargs={'capability_id': obj.id})

class CapabilityCreate(CreateView):
    model = Capability
    form_class = CapabilityForm
    template_name_suffix = '_update'
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
        self.object.delete()
        return HttpResponse('Deleted')
