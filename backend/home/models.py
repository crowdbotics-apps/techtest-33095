from django.conf import settings
from django.db import models


class Teacher(models.Model):
    "Generated Model"
    name = models.CharField(
        max_length=256,
    )
    email = models.CharField(
        max_length=256,
    )
    department = models.CharField(
        max_length=256,
    )
    phone = models.FloatField()


class Student(models.Model):
    "Generated Model"
    name = models.CharField(
        max_length=256,
    )
    email = models.EmailField(
        max_length=254,
    )
    department = models.CharField(
        max_length=256,
    )
    phone = models.FloatField()
