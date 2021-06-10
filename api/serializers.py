from rest_framework import serializers

class Studentserializer(serializers.Serializer):
    name=serializers.CharField(max_length=256)
    roll=serializers.IntegerField()
    mark=serializers.IntegerField()