# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Usuario,Categoria,Noticia
from django.contrib.auth.models import User

# Register your models here.


admin.site.register(Usuario)
admin.site.register(Categoria)



class FilterUserAdmin(admin.ModelAdmin): 
    def save_model(self, request, obj, form, change):
        obj.user = request.user
        obj.save()

    def get_queryset(self, request):

        
        qs = super(FilterUserAdmin, self).get_queryset(request) 
        if(request.user.is_superuser):
        	return qs.filter()
        else:
        	return qs.filter(usuario__name =request.user)


class MyModelAdmin(FilterUserAdmin):
	list_display=['titulo','seccion','usuario','fecha']
	list_filter=['seccion','fecha','usuario']
admin.site.register(Noticia, MyModelAdmin)
