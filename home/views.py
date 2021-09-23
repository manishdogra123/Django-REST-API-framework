from django.shortcuts import render
from rest_framework.views import ApiView
from rest_framework.response import Response
from .models import Course,Courseserializer


# Create your views here.
class Courselistview(ApiView):
    def get(self):
        course = Course.objects.all()
        serializer = Courseserializer(course, many=True)
        return Response(serializer.data)
       