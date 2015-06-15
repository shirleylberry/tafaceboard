#forms.py
from django import forms
from django.forms import ModelForm
from django.forms.fields import Field
from tutorboard.models import Tutor, Capability, Subject
from django.forms import CheckboxSelectMultiple, TextInput, HiddenInput, Textarea

setattr(Field, 'is_hidden', lambda self: isinstance(self.widget, forms.HiddenInput ))

BIRTH_YEAR_CHOICES = ('1980', '1981', '1982')
FAVORITE_COLORS_CHOICES = (('blue', 'Blue'),
                            ('green', 'Green'),
                            ('black', 'Black'))
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
        widgets = {
            'bioline1': TextInput(attrs={'class':'update-bio'}),
            'bioline2': TextInput(attrs={'class':'update-bio'}),
            'bioline3': TextInput(attrs={'class':'update-bio'}),
            'bioline4': TextInput(attrs={'class':'update-bio'}),
            'bioline5': TextInput(attrs={'class':'update-bio'}),
            'energy': CheckboxSelectMultiple(attrs={'class':'update-checkbox'}),
            'presence': CheckboxSelectMultiple(attrs={'class':'update-checkbox'}),
            'archetype': CheckboxSelectMultiple(attrs={'class':'update-checkbox'}),
            'location': CheckboxSelectMultiple(attrs={'class':'update-checkbox'}),
            'styles': CheckboxSelectMultiple(attrs={'class':'update-checkbox'}),
            'levelPreferences': CheckboxSelectMultiple(attrs={'class':'update-checkbox'}),
            'studentEngagements': CheckboxSelectMultiple(attrs={'class':'update-checkbox'}),
            'skills': CheckboxSelectMultiple(attrs={'class':'update-checkbox'}),
            'highestLevel': HiddenInput(),
            'availability_note':Textarea(attrs={'rows':'4', 'cols':'40'}),
            'availability_vacation':Textarea(attrs={'rows':'4', 'cols':'40'}),
            'sex': HiddenInput(),
        }

class AvailabilityForm(forms.ModelForm):
    class Meta:
        model = Tutor
        fields = ['fname', 'lname', 'availability', ]


class SubjectForm(forms.ModelForm):
    class Meta:
        model = Subject


class CapabilityForm(forms.ModelForm):
     
    class Meta: 
        model = Capability
        widgets = {            
            'score': TextInput(attrs={'size':'4'}),
            'notes': Textarea(attrs={'rows':'4', 'cols':'40'}),
        }