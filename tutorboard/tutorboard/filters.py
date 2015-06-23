from models import Tutor, Capability, Subject
from django_filters import FilterSet, MultipleChoiceFilter, ModelMultipleChoiceFilter

class TutorFilter(FilterSet):
    gender = MultipleChoiceFilter(conjoined=True, name='gender')
    area = MultipleChoiceFilter(conjoined=True, name='area')

    subject = ModelMultipleChoiceFilter(conjoined=True, name='capabilities__subject__name')

    class Meta:
        model = Tutor
        fields = ['capabilities__subject__name']

