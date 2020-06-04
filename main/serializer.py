from rest_framework import serializers
from .models import *

class MemberSerialiser(serializers.ModelSerializer):

    class Meta:
        model = TeamMember
        fields = '__all__'

class EventSerialiser(serializers.ModelSerializer):

    class Meta:
        model = Events
        fields = '__all__'

class MailSerialiser(serializers.ModelSerializer):

    class Meta:
        model = Email
        fields = '__all__'