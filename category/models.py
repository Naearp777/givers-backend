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

    def __str__(self):
        return f'{self.province}'


class District(models.Model):
    district = models.CharField(null=True, unique=True, max_length=100)

    def __str__(self):
        return f'{self.district}'


class Municipality(models.Model):
    Municipality = models.CharField(null=True, unique=True, max_length=100)

    def __str__(self):
        return f'{self.Municipality}'


class Ward(models.Model):
    ward = models.CharField(null=True, unique=True, max_length=100)

    def __str__(self):
        return f'{self.ward}'


class Skills(models.Model):
    skills = models.CharField(null=True, unique=True, max_length=100)

    def __str__(self):
        return f'{self.skills}'
