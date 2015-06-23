from models import Tutor, Capability, Subject, AREA, GENDER
from django_filters import FilterSet, MultipleChoiceFilter, ModelMultipleChoiceFilter, BooleanFilter

class AreaChoiceFilter(MultipleChoiceFilter):
    def filter(self, qs, value):
        if 'math' in value or 'verbal' in value:
            value.append('crossover')
        return super(AreaChoiceFilter, self).filter(qs, value)

class TutorFilter(FilterSet):
    gender = MultipleChoiceFilter(choices=GENDER)
    area = AreaChoiceFilter(choices=AREA)
    hidden = BooleanFilter()
    #subject = ModelMultipleChoiceFilter(name='capabilities__subject__name')

    class Meta:
        model = Tutor
        fields = ['area', 'gender', 'hidden'] # 'subject'

