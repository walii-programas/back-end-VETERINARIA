from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import permissions
from api.serializers import VeterinarioSerializer, ServiciosSerializer, BlogSerializer
from veterinaria.models import Veterinario, Servicios, Blog
# from django.http import HttpResponse

# Create your views here.
class VeterinarioViewSet(viewsets.ModelViewSet):
    queryset = Veterinario.objects.all()
    serializer_class = VeterinarioSerializer
    permission_classes = [permissions.IsAuthenticated]
    

class ServiciosViewSet(viewsets.ModelViewSet):
    queryset = Servicios.objects.all()
    serializer_class = ServiciosSerializer
    permission_classes = [permissions.IsAuthenticated]


class BlogViewSet(viewsets.ModelViewSet):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    permission_classes = [permissions.IsAuthenticated]
  

