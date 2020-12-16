from django.db import models

# Create your models here.

class Persona(models.Model):
    id_persona = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50,blank=False,null=False)
    apellido = models.CharField(max_length=50,blank=False,null=False)
