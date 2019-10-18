from django.db import models
from datetime import date

# Create your models here.
class TestModel(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    dob = models.DateField(default=date.today)
    email = models.EmailField(max_length=255, unique=True)

    def __str__(self):
        return self.first_name + self.last_name
