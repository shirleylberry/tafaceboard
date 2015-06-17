from rest_framework import serializers
from django.contrib.auth.models import User
from tutorboard.models import Tutor, Capability, Subject

class CapabilitySerializer(serializers.ModelSerializer):
    class Meta():
        model = Capability
        fields = ('level', 'level_note', 'score', 'area', 'notes', 'subject', 'tutor')

