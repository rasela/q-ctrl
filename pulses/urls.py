from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from pulses import views

urlpatterns = [
    path('pulses/', views.PulseList.as_view()),
    path('pulses/<int:pk>/', views.PulseDetail.as_view()),
    path('pulses/download', views.PulsesCSVExportView.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)