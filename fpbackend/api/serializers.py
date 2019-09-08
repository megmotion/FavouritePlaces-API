from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Place


class PlaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Place
        fields = ['id', 'name', 'link', 'address', 'description']

class PlaceMiniSerializer(serializers.ModelSerializer):
    class Meta:
        model = Place
        fields = ['id', 'name']
