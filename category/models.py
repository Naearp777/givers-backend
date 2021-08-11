from django.db import models

# Create your models here.


class EventCategory(models.Model):
    category = models.CharField(null=True, unique=True, max_length=100)

    def __str__(self):
        return f'{self.category}'


class Country(models.Model):
    country = models.CharField(null=True, unique=True, max_length=100)

    def __str__(self):
        return f'{self.country}'


class Province(models.Model):
    province = models.CharField(null=True, unique=True, max_length=100)
    country = models.ForeignKey(Country, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f'{self.province}'


class District(models.Model):
    district = models.CharField(null=True, unique=True, max_length=100)
    province = models.ForeignKey(Province, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f'{self.district}'


class Municipality(models.Model):
    Municipality = models.CharField(null=True, unique=True, max_length=100)
    district = models.ForeignKey(District, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f'{self.Municipality}'


class Ward(models.Model):
    ward = models.PositiveSmallIntegerField(
        null=True, unique=True)
    municipality = models.ForeignKey(
        Municipality, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f'{self.ward}'


class Skills(models.Model):
    skills = models.CharField(null=True, unique=True, max_length=100)

    def __str__(self):
        return f'{self.skills}'
