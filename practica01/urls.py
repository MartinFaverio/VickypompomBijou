# Importamos librerias
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('portfolio/', views.portfolio, name='portfolio'),
    path('mensaje/', views.mensaje, name='mensaje'),
    path('contact/', views.contact, name="contact"),
]
