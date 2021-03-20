from django.contrib.auth.models import User
from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields.reverse_related import ManyToOneRel


class UserInfo(models.Model):
    user = models.ForeignKey(User, on_delete=CASCADE)
    title = models.CharField(max_length=50)
    category = models.CharField(max_length=50)
    skills = models.CharField(max_length=50)
    expertiseRadio = models.CharField(max_length=50)
    company = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    zip = models.CharField(max_length=50)
    designation = models.CharField(max_length=50)
    description = models.CharField(max_length=500)
    university = models.CharField(max_length=50)
    areaOfStudy = models.CharField(max_length=50)
    degree = models.CharField(max_length=50)
    certification = models.CharField(max_length=50)
    language = models.CharField(max_length=50)
    proficiency = models.CharField(max_length=50)
    hourlyPrice = models.CharField(max_length=50)
    fixedPrice = models.CharField(max_length=50)
    country = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.title} and {self.category}"
