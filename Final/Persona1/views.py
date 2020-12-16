from django.shortcuts import render, HttpResponse
import json
# Create your views here.
from django.http.response import JsonResponse
from Persona1.models import Persona
from django.core import serializers
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.parsers import JSONParser 
from Persona1.serial import PersonaSerial


@api_view(['GET'])
def getAll_persona(request):
    
    #personas = Persona.objects.all()

    #personas_serial = PersonaSerial(personas)
    #return JsonResponse(personas_serial.data,status = status.HTTP_200_OK)
    
    #persona_json = serializers.serialize("json", Persona.objects.all())
    #data = {"Persona_json": persona_json}

    
    return JsonResponse(serializers.serialize("json", Persona.objects.all()),safe = False,status = status.HTTP_200_OK)
 

@api_view(['GET'])
def getByID_persona(request,id_persona):
  
    return JsonResponse(PersonaSerial(Persona.objects.get(id_persona = id_persona)).data,safe = False,status = status.HTTP_200_OK)


@api_view(['POST'])
def post_persona(request):
    
    persona = PersonaSerial(data = JSONParser().parse(request))
    if persona.is_valid(): 
        persona.save()       
        return JsonResponse(persona.data,status = status.HTTP_201_CREATED)

@api_view(['PUT']) 
def put_persona(request,id_persona):

    data = JSONParser().parse(request)

    persona_serial = PersonaSerial(Persona.objects.get(id_persona = id_persona),data = data)

    if persona_serial.is_valid():
        persona_serial.save()
    return JsonResponse(persona_serial.data,status = status.HTTP_202_ACCEPTED)

@api_view(['DELETE'])
def eliminar_persona(request,id_persona):

    Persona.objects.get(id_persona = id_persona).delete()   

    return JsonResponse({'message':'Persona eliminada'},status = status.HTTP_200_OK)
