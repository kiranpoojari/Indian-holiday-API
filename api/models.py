from django.db import models

class Holiday(models.Model):
    name = models.CharField(max_length=200)
    date = models.DateField()
    local_name = models.CharField(max_length=200)
    country_code = models.CharField(max_length=10)
    types = models.CharField(max_length=100)
