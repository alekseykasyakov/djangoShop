from django.db import models

# Create your models here.


class Language(models.Model):
    languages_id = models.PositiveSmallIntegerField()
    name = models.CharField(max_length=50)
    code = models.CharField(max_length=5)
    image = models.CharField(max_length=255)
    directory = models.CharField(max_length=50)
    sort_order = models.PositiveSmallIntegerField()

