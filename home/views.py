from django.http.request import RAISE_ERROR
from django.http.response import JsonResponse
from django.shortcuts import render
from rest_framework.serializers import Serializer
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Course
from django.http import Http404
from .serializer import Courseserializer
from rest_framework import status


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

class Courselist_detail(APIView):
    def get_object(self,pk):
        try:
            return Course.objects.get(pk=pk)
        except Course.DoesNotExist:
            raise Http404
    def get(self,request,pk,formet=None):
        course_tutorial = self.get_object(pk)
        serializer = Courseserializer(course_tutorial)
        return Response(serializer.data)

    def delete(self,request,pk,formet=None):
        Serializer = self.get_object(pk)
        Serializer.delete() 
        return Response(status=status.HTTP_204_NO_CONTENT)
    def put(self,request,pk,formet=None):
        User_deatil = self.get_object(pk)
        Serializer = Courseserializer(User_deatil,data=request.data)
        if Serializer.is_valid():
            Serializer.save()
        return Response(status=status.HTTP_400_BAD_REQUEST)    
