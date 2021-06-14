# from django.shortcuts import render
# from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from rest_framework.generics import ( ListAPIView, RetrieveAPIView, UpdateAPIView, RetrieveUpdateAPIView, ListCreateAPIView)

from api import serializers, models

class ArticlesListView(ListCreateAPIView):
    queryset=models.Article.objects.all()
    serializer_class= serializers.ArticleSerializer

class ArticlesDetailView(RetrieveUpdateAPIView):
    queryset=models.Article.objects.all()
    serializer_class= serializers.ArticleSerializer




    

