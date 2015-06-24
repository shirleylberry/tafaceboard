# forms.py
from django import forms
from django.forms.fields import Field
from django.forms.models import modelformset_factory
from django.forms import TextInput, HiddenInput, Textarea

from tutorboard.models import Tutor, Capability, Subject


setattr(Field, 'is_hidden', lambda self: isinstance(self.widget, forms.HiddenInput))

AVAILABILITY_CHOICES = [('zero', '0 - 5'),('five','5 - 10'),('ten','10 - 15')]
LEVEL_CHOICES = [('PR','Professional'),('EX','Expert'),('DR','Director')]
SUBJECT_CHOICES = [('cornerstone','Cornerstone'),('echelon','Echelon'),('sat','SAT'),('academic','Academic')]

class SearchForm(forms.Form):
    availability = forms.ChoiceField(widget=forms.RadioSelect, choices=AVAILABILITY_CHOICES, required=False)
    level = forms.ChoiceField(widget=forms.RadioSelect, choices=LEVEL_CHOICES, required=False)
    subject = forms.ChoiceField(widget=forms.RadioSelect, choices=SUBJECT_CHOICES, required=False)
    search = forms.CharField(required=False)


class TutorForm(forms.ModelForm):
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
            'hidden'

            #'availability_updated',
            ]
        widgets = {
            'bioline1': TextInput(attrs={'class': 'update-bio'}),
            'bioline2': TextInput(attrs={'class': 'update-bio'}),
            'bioline3': TextInput(attrs={'class': 'update-bio'}),
            'bioline4': TextInput(attrs={'class': 'update-bio'}),
            'bioline5': TextInput(attrs={'class': 'update-bio'}),
            'highestLevel': HiddenInput(),
            'availability_note': Textarea(attrs={'rows': '4', 'cols': '40'}),
            'availability_vacation': Textarea(attrs={'rows': '4', 'cols': '40'}),
        }


class AvailabilityForm(forms.ModelForm):
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
        fields = ['level', 'level_note', 'score', 'area', 'notes', 'subject', 'tutor', 'id']
        widgets = {
            'score': TextInput(attrs={'size': '4'}),
            'notes': Textarea(attrs={'rows': '4', 'cols': '40'}),
            'tutor': HiddenInput(),
            'subject': HiddenInput(),
        }

CapabilityFormSet = modelformset_factory(Capability)
