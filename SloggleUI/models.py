from django.db import models


class UserInfo(models.Model):
    title = models.CharField(max_length=50)
    category = models.CharField(max_length=50)
    skills = models.CharField(max_length=50)
    expertiseRadio = models.CharField(max_length=50)
    company = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    zip = models.CharField(max_length=50)
    designation = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.title} and {self.category}"
