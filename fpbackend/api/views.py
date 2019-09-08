from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from .serializers import PlaceSerializer, PlaceMiniSerializer
from .models import Place
from rest_framework.response import Response

class PlaceViewSet(viewsets.ModelViewSet):
    queryset = Place.objects.all()
    serializer_class = PlaceSerializer

    def list(self, request, *args, **kwargs):
    	places = Place.objects.all()
    	serializer = PlaceMiniSerializer(places, many=True)
    	return Response(serializer.data)