from rest_framework import serializers

from api import models

class Studentserializer(serializers.Serializer):
    name=serializers.CharField(max_length=256)
    roll=serializers.IntegerField()
    marks=serializers.IntegerField()

class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model=models.Article
        fields="__all__"