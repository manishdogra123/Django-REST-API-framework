from django.db.models import fields
from .models import Course
from rest_framework import serializers


class Courseserializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'
