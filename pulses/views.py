from django.shortcuts import render
from rest_framework import generics
from .models import Pulse
from .serializers import PulseSerializer

import csv
from django.http import HttpResponse

class PulseList(generics.ListCreateAPIView):
    queryset = Pulse.objects.all()
    serializer_class = PulseSerializer

class PulseDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Pulse.objects.all()
    serializer_class = PulseSerializer

class PulsesCSVExportView(generics.ListCreateAPIView):

    serializer_class = PulseSerializer
    
    def get_serializer(self, queryset, many=True):
        return self.serializer_class(
            queryset,
            many=many,
        )

    def get(self, request, *args, **kwargs):
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="export.csv"'
        
        serializer = self.get_serializer(
            Pulse.objects.all(),
            many=True
        )
        header = PulseSerializer.Meta.fields
        
        writer = csv.DictWriter(response, fieldnames=header)
        writer.writeheader()
        for row in serializer.data:
            writer.writerow(row)
        
        return response