from django.db import models

# Create your models here.
class CountryList(models.Model):
    name = models.CharField(max_length= 256)
    countryid = models.BigIntegerField()

    def __str__(self):
        return self.name