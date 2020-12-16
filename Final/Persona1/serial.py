from rest_framework import serializers
from Persona1.models import Persona

#DTO
class PersonaSerial(serializers.ModelSerializer):

    class Meta:
        model = Persona
        fields = ('id_persona','nombre','apellido')

