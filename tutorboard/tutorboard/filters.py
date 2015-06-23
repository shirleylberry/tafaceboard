from models import Tutor, Capability, Subject, AREA, GENDER, AVAILABILITY
from django_filters import FilterSet, MultipleChoiceFilter, ModelMultipleChoiceFilter, BooleanFilter, ModelChoiceFilter, ChoiceFilter

class AreaChoiceFilter(MultipleChoiceFilter):
    def filter(self, qs, value):
        if 'math' in value or 'verbal' in value:
            value.append('crossover')
        return super(AreaChoiceFilter, self).filter(qs, value)

class TutorFilter(FilterSet):
    area = AreaChoiceFilter(choices=AREA)
    subjects = ModelMultipleChoiceFilter
    availability = ChoiceFilter(choices=AVAILABILITY, lookup_type='gt')
    gender = MultipleChoiceFilter(choices=GENDER)
    hidden = BooleanFilter()

    class Meta:
        model = Tutor
        fields = ['area', 'gender', 'hidden', 'subjects', 'availability']

