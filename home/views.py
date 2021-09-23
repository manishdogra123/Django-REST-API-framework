from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Course
from .serializer import Courseserializer


# Create your views here.
class Courselistview(APIView):
    def get(self,request,formet=None):
        courses = Course.objects.all()
        serializer = Courseserializer(courses, many=True)
        return Response(serializer.data)
    def post(self,request,formet=None):
        serializer = Courseserializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)              