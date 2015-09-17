# forms.py
from django import forms
from django.forms.fields import Field
from django.forms.models import modelformset_factory
from django.forms import TextInput, HiddenInput, Textarea, ChoiceField, RadioSelect, CheckboxInput, CheckboxSelectMultiple, ModelMultipleChoiceField

from tutorboard.models import Tutor, Capability, Subject, HiredFor, ProDevelopment


setattr(Field, 'is_hidden', lambda self: isinstance(self.widget, forms.HiddenInput))

AVAILABILITY_CHOICES = [('zero', '0 - 5'), ('five', '5 - 10'), ('ten', '10 - 15')]
LEVEL_CHOICES = [('PR', 'Professional'), ('EX', 'Expert'), ('DR', 'Director')]
SUBJECT_CHOICES = [('cornerstone', 'Cornerstone'), ('echelon', 'Echelon'), ('sat', 'SAT'), ('academic', 'Academic')]

class SearchForm(forms.Form):
    availability = forms.ChoiceField(widget=forms.RadioSelect, choices=AVAILABILITY_CHOICES, required=False)
    level = forms.ChoiceField(widget=forms.RadioSelect, choices=LEVEL_CHOICES, required=False)
    subject = forms.ChoiceField(widget=forms.RadioSelect, choices=SUBJECT_CHOICES, required=False)
    search = forms.CharField(required=False)


class TutorForm(forms.ModelForm):
    #hired_for = ModelMultipleChoiceField(queryset=HiredFor.objects.all(), to_field_name='name')
    #pro_development = ModelMultipleChoiceField(queryset=ProDevelopment.objects.all(), to_field_name='name')

    def __init__(self, *args, **kwargs):
        super(TutorForm, self).__init__(*args, **kwargs)
        self.fields['hired_for'].required = False
        self.fields['pro_development'].required = False

    class Meta:
        model = Tutor
        fields = [
            'picture',
            'fname',
            'lname',

            'availability',
            'availability_note',
            'availability_vacation',

            'area',


            'gotofor',
            'tags',
            'bioline1',
            'bioline2',
            'bioline3',
            'bioline4',
            'bioline5',
            'highestLevel',
            'highestLevelManual',

            'gender',
            'email',
            'altemail',

            'cell',
            'altphone',

            'address1',
            'address2',
            'city',
            'state',
            'zip',
            'neighborhood',
            'hidden',

            'hired_for',
            'pro_development'


            #'availability_updated',
            ]
        widgets = {



            #'picture':              TextInput(attrs={'class': 'form-control'}),
            'fname':                TextInput(attrs={'class': 'form-control'}),
            'lname':                TextInput(attrs={'class': 'form-control'}),

            'availability':         TextInput(attrs={'class': 'form-control'}),
            'availability_note':    Textarea(attrs={'rows': '4', 'cols': '40', 'class': 'form-control'}),
            'availability_vacation': Textarea(attrs={'rows': '4', 'cols': '40', 'class': 'form-control'}),

            'area':                 RadioSelect(attrs={'class': 'form-control'}),
            'gotofor':              TextInput(attrs={'class': 'form-control'}),
            'bioline1':             TextInput(attrs={'class': 'form-control'}),
            'bioline2':             TextInput(attrs={'class': 'form-control'}),
            'bioline3':             TextInput(attrs={'class': 'form-control'}),
            'bioline4':             TextInput(attrs={'class': 'form-control'}),
            'bioline5':             TextInput(attrs={'class': 'form-control'}),
            'highestLevel':         HiddenInput(),
            'highestLevelManual':   RadioSelect(attrs={'class': 'form-control'}),



            'gender':               RadioSelect(attrs={'class': 'form-control'}),
            'email':                TextInput(attrs={'class': 'form-control'}),
            'altemail':             TextInput(attrs={'class': 'form-control'}),
            'cell':                 TextInput(attrs={'class': 'form-control'}),
            'altphone':             TextInput(attrs={'class': 'form-control'}),

            'address1':             TextInput(attrs={'class': 'form-control'}),
            'address2':             TextInput(attrs={'class': 'form-control'}),
            'city':                 TextInput(attrs={'class': 'form-control'}),
            'state':                TextInput(attrs={'class': 'form-control'}),
            'zip':                  TextInput(attrs={'class': 'form-control'}),

            'neighborhood':         TextInput(attrs={'class': 'form-control'}),
            #'hidden':               CheckboxInput(attrs={'class': 'form-control'}),
        }


class AvailabilityForm(forms.ModelForm):

    def clean_availability(self):
        availability = self.cleaned_data.get('availability')
        if availability is None:
            return 0
        else:
            return availability

    class Meta:
        model = Tutor
        fields = ['fname', 'lname', 'availability', ]


class SubjectForm(forms.ModelForm):
    class Meta:
        model = Subject
        fields = ['name', 'image', 'is_ap', 'imageAP']


class CapabilityForm(forms.ModelForm):

    class Meta:
        model = Capability
        fields = ['level', 'score', 'area', 'level_note', 'notes', 'subject', 'tutor', 'id']
        widgets = {
            'score': TextInput(attrs={'size': '4'}),
            'notes': Textarea(attrs={'rows': '4', 'cols': '30'}),
            'level_note': Textarea(attrs={'rows': '4', 'cols': '30'}),
            'tutor': HiddenInput(),
            'subject': HiddenInput(),
        }

CapabilityFormSet = modelformset_factory(Capability)
