# from django.shortcuts import render
# from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response
from api import serializers

import json
# Create your views here.

class Student:
    def __init__(self, name, roll, marks):
        self.name=name
        self.roll=roll
        self.marks=marks

@api_view()
def apiusers(request):
    student1=Student("Santhosh",1,98)
    student2=Student("Gokul",2,99)
    student3=Student("Kumar",3,97)
    response=serializers.Studentserializer([student1,student2,student3], many=True)
    return Response(response.data)
    

