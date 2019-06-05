from django.db import models
from django.core.validators import MaxValueValidator
from django.core.validators import MinValueValidator

class Pulse(models.Model):
    TYPE_CHOICES = (
        ('primitive', 'Primitive'),
        ('corpse', 'CORPSE'),
        ('gaussian', 'Gaussian'),
        ('cinbb', 'CinBB'),
        ('cinsk', 'CinSK'),
    )
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=100, blank=True, default='')   
    type = models.CharField(choices=TYPE_CHOICES, default='Primitive', max_length=100)
    maximum_rabi_rate = models.PositiveIntegerField(default=0, validators=[MaxValueValidator(20),])
    polar_angle = models.DecimalField(decimal_places=1,max_digits=2, default="0.1", validators=[MaxValueValidator(1), MinValueValidator(0),])

    class Meta:
        ordering = ('created',)

    def __str__(self):
        return self.name