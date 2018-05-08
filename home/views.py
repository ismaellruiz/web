# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .models import Noticia
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import DetailView

# Create your views here.
def qsomos(request):
	rw1 = Noticia.objects.filter(seccion=1)[:10][::-1]
	rw2 = Noticia.objects.filter(seccion=2)[:10][::-1]
	rw3 = Noticia.objects.filter(seccion=3)[:10][::-1]





	return render(request,"quienes.html",{"rw1":rw1,"rw2":rw2,"rw3":rw3})





def Imprimir_noticia(request):
	noticia = Noticia.objects.all()
	page = request.GET.get('page', 1)
	paginator = Paginator(noticia, 10)
	try:
		users = paginator.page(page)
	except PageNotAnInteger:
		users = paginator.page(1)
	except EmptyPage:
		users = paginator.page(paginator.num_pages)

	return render(request,'noticias.html',{'noticia': noticia} )

class Detail_noticia(DetailView):
	template_name = "noticia.html"
	model = Noticia