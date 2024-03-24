from django.db import models
from users.models import User
from django.core.validators import MinValueValidator, MaxValueValidator

# Constants
NULLABLE = {'blank': True, 'null': True}


# Location
class Location(models.Model):
    '''Location model'''

    city = models.CharField(max_length=100, verbose_name='Город', **NULLABLE)
    state = models.CharField(max_length=100, verbose_name='Штат', **NULLABLE)
    zip_code = models.CharField(max_length=5, verbose_name='Почтовый индекс', **NULLABLE)
    latitude = models.DecimalField(max_digits=9, decimal_places=5, verbose_name='Широта', **NULLABLE)
    longitude = models.DecimalField(max_digits=9, decimal_places=5, verbose_name='Долгота', **NULLABLE)

    def __str__(self):
        return f'{self.city}, {self.state}, {self.zip_code}'

    class Meta:
        verbose_name = 'Локация'
        verbose_name_plural = 'Локации'


# Cargo
class Cargo(models.Model):
    '''Cargo model'''

    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Автор', **NULLABLE)
    pick_up_location = models.ForeignKey(Location, related_name='pick_up_cargos', on_delete=models.CASCADE, **NULLABLE)
    delivery_location = models.ForeignKey(Location, related_name='delivery_cargos', on_delete=models.CASCADE,
                                          **NULLABLE)

    weight = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(1000)], verbose_name='Вес груза',
                                 **NULLABLE)
    description = models.TextField(verbose_name='Описание груза', **NULLABLE)

    def __str__(self):
        return f'{self.pk}, {self.description}, {self.weight}'

    class Meta:
        verbose_name = 'Груз'
        verbose_name_plural = 'Грузы'


# Car
class Car(models.Model):
    '''Car model'''

    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Автор', **NULLABLE)
    current_location = models.ForeignKey(Location, on_delete=models.CASCADE, **NULLABLE)

    unique_number = models.CharField(max_length=5, unique=True, **NULLABLE)
    cargo_capacity = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(1000)],
                                         verbose_name='Грузоподъемность', **NULLABLE)

    def __str__(self):
        return f'{self.unique_number}, {self.cargo_capacity}'

    class Meta:
        verbose_name = 'Машина'
        verbose_name_plural = 'Машины'
