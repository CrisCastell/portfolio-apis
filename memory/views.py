from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Animal
import random

# Create your views here.
@csrf_exempt
def animals(request):

    animalList = Animal.objects.all()
    animals1 = [animal.serialize() for animal in animalList]
    animals2 = [animal.serialize() for animal in animalList]
    animals = animals1 + animals2
    random.shuffle(animals)
    return JsonResponse(animals, safe=False)