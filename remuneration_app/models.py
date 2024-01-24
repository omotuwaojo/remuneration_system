from django.db import models

# Create your models here.
# remuneration_app/models.py

class Employee(models.Model):
    name = models.CharField(max_length=100)
    department =models.CharField(default='Default Department', max_length=100)
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    performance_score = models.IntegerField()

    def __str__(self):
        return self.name
