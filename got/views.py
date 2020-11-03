from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import CharacterSerializer, HouseSerializer
from .models import Character, House

# Create your views here.

@api_view(['GET'])
def charList(request):
    characters = Character.objects.all()
    serializer = CharacterSerializer(characters, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def houseList(request):
    houses = House.objects.all()
    serializer = HouseSerializer(houses, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def characters(request, pk):
    characters = Character.objects.filter(house=pk)
    serializer = CharacterSerializer(characters, many=True)
    return Response(serializer.data)