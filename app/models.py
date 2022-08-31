from django.db import models
from django.conf import settings
from django.core.validators import RegexValidator

# Create your models here.
class Person(models.Model):
    name = models.CharField(max_length=100, verbose_name="full name")
    age = models.IntegerField()
    phone_regex = RegexValidator(regex=r'^\+?1?\d{10,11}$', message="Phone number must be entered in the format: '+9999999999'. Up to 10 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], max_length=10, blank=True) 
    address = models.TextField()

    def __str__(self):
        return self.name
