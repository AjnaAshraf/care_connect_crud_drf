from rest_framework import serializers
from staff.models import Doctor

class DoctorSerializer(serializers.Serializer):

    id = serializers.CharField(read_only=True)

    name=serializers.CharField()

    specialization = serializers.ChoiceField(Doctor.SPECIALIZATION_OPTIONS)

    fee = serializers.IntegerField()

    email = serializers.EmailField()