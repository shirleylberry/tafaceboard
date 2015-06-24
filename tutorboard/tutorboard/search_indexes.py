import datetime
from haystack import indexes
from models import Tutor, Subject, Capability


class TutorIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)

    fname = indexes.CharField(model_attr='fname')
    lname = indexes.CharField(model_attr='lname')
    # Contact
    cell = indexes.CharField(model_attr='cell')
    altphone = indexes.CharField(model_attr='altphone')
    email = indexes.CharField(model_attr='email')
    altemail = indexes.CharField(model_attr='altemail')
    address1 = indexes.CharField(model_attr='address1')
    address2 = indexes.CharField(model_attr='address2')
    city = indexes.CharField(model_attr='city')
    state = indexes.CharField(model_attr='state')
    zip = indexes.CharField(model_attr='zip')
    neighborhood = indexes.CharField(model_attr='neighborhood')

    # Bio
    gotofor = indexes.CharField(model_attr='gotofor')
    bioline1 = indexes.CharField(model_attr='bioline1')
    bioline2 = indexes.CharField(model_attr='bioline2')
    bioline3 = indexes.CharField(model_attr='bioline3')
    bioline4 = indexes.CharField(model_attr='bioline4')
    bioline5 = indexes.CharField(model_attr='bioline5')

    availability_note = indexes.CharField(model_attr='availability_note')
    availability_vacation = indexes.CharField(model_attr='availability_vacation')

    subjects = indexes.MultiValueField()

    def get_model(self):
        return Tutor

    def prepare_subjects(self, obj):
        # Since we're using a M2M relationship with a complex lookup,
        # we can prepare the list here.
        return [subject.name for subject in obj.subjects.all()]
