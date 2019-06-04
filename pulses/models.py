from django.db import models
from django.core.validators import MaxValueValidator

class Pulse(models.Model):
    TYPE_CHOICES = (
        ('P', 'Primitive'),
        ('C', 'CORPSE'),
        ('G', 'Gaussian'),
        ('CB', 'CinBB'),
        ('CS', 'CinSK'),
    )
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=100, blank=True, default='')   
    type = models.CharField(choices=TYPE_CHOICES, default='Primitive', max_length=100)
    maximum_rabi_rate = models.PositiveIntegerField(default=0, validators=[MaxValueValidator(20),])
    polar_angle = models.CharField(max_length=100, blank=True, default='')

    class Meta:
        ordering = ('created',)

    def __str__(self):
        return self.name