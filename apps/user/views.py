from django.shortcuts import render

# Create your views here.
from rest_framework.generics import CreateAPIView
from . import serializer

class RegisterView(CreateAPIView):
    serializer_class = serializer.RegisterSerializer