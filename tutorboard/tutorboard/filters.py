from models import Tutor, Capability, Subject, AREA, GENDER, AVAILABILITY, LEVEL
from django_filters import FilterSet, MultipleChoiceFilter, ModelMultipleChoiceFilter, BooleanFilter, ModelChoiceFilter, ChoiceFilter
from django import forms

SORT = (
    ('magic', 'Magic'),
    ('-availability', 'Most available'),
    ('availability', 'Least available'),
    ('fname', 'Name'),
    ('level', 'Level'),
)

# TutorFilter adds the rest of the options to this form,
# but the sort option doesn't act on any field of Tutor, so it needs to
# be in a parent form that the TutorFilter uses.
class TutorFilterForm(forms.Form):
    sort = forms.ChoiceField(widget=forms.RadioSelect, choices=SORT, required=False)

class AreaChoiceFilter(MultipleChoiceFilter):
    def filter(self, qs, value):
        if 'math' in value or 'verbal' in value:
            value.append('crossover')
        return super(AreaChoiceFilter, self).filter(qs, value)

class LevelChoiceFilter(ChoiceFilter):
    def filter(self, qs, value):
        _qs = qs
        _value = value
        if value == u'no':
            value = u''
        filter = super(LevelChoiceFilter, self).filter(qs, value)
        return filter




class TutorFilter(FilterSet):
    area = AreaChoiceFilter(choices=AREA)
    subjects = ModelMultipleChoiceFilter
    hired_for = ModelMultipleChoiceFilter
    pro_development = ModelMultipleChoiceFilter
    availability = ChoiceFilter(choices=AVAILABILITY, lookup_type='gt')
    gender = MultipleChoiceFilter(choices=GENDER)
    hidden = BooleanFilter()
    highestLevelManual = LevelChoiceFilter(choices=LEVEL, label='Level')



    class Meta:
        model = Tutor
        form = TutorFilterForm
        fields = ['area', 'gender', 'hidden', 'subjects', 'availability', 'hired_for', 'pro_development', 'highestLevelManual']

