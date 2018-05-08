"""Conalep URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path(r'$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path(r'$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  path(r'blog/', include('blog.urls'))
"""
from django.urls import path
from django.conf.urls import url
from django.contrib import admin
from home import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path(r'admin/', admin.site.urls),
    path(r'', views.qsomos, name="home_view"),
    path(r'noticias/', views.Imprimir_noticia,name="Imprimir_noticias"),
    url(r'noticia/(?P<pk>\d+)/',views.Detail_noticia.as_view(),name='detail_noticia_view'),
    path(r'frm', views.Imprimir_noticia, name="forma_view"),
    #path(r'mensaje/',views.Mensaje,name="Mensaje"),

]
if settings.DEBUG:
	urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)