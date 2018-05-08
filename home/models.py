# -*- coding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Usuario(models.Model):
	name = models.OneToOneField(User,on_delete=models.CASCADE)
	telefono = models.IntegerField()
	correo = models.CharField(max_length=48)
	area= models.CharField(max_length=50)


	def __str__(self):
 		return ("%s") % self.name

class Categoria(models.Model):
	nombre = models.CharField(max_length=15)

	def __str__(self):
		return ("%s") % self.nombre


class Noticia(models.Model):
	usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
	fecha = models.DateField(auto_now=True)
	seccion = models.ForeignKey(Categoria,on_delete=models.CASCADE)
	titulo = models.CharField(max_length=30)
	datos = models.CharField(max_length=500)
	imagen = models.ImageField(null=True, blank=True)


	def __str__(self):
		return ("%s") % self.titulo

class Mensaje(models.Model):
	titulo = models.CharField(max_length=50)
	fecha = models.DateTimeField(auto_now=True)
	correo= models.CharField(max_length=30)
	datos = models.CharField(max_length=100)



	def __str__(self):
		return ("%s - %s") % (self.titulo, self.correo )
