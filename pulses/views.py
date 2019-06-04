from django.shortcuts import render
from rest_framework import generics
from .models import Pulse
from .serializers import PulseSerializer

class PulseList(generics.ListCreateAPIView):
    queryset = Pulse.objects.all()
    serializer_class = PulseSerializer


class PulseDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Pulse.objects.all()
    serializer_class = PulseSerializer