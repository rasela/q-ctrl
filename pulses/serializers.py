from rest_framework import serializers
from .models import Pulse


class PulseSerializer(serializers.ModelSerializer):

    class Meta:
        model = Pulse
        fields = ('id', 'name', 'type', 'maximum_rabi_rate',
                  'polar_angle', )