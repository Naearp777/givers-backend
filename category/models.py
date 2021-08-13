from django.db import models

# Create your models here.


class EventCategory(models.Model):
    category = models.CharField(null=True, unique=True, max_length=100)

    def __str__(self):
        return f'{self.category}'

    class Meta:
        verbose_name_plural = "Event categories"


class Country(models.Model):
    country = models.CharField(null=True, unique=True, max_length=100)

    def __str__(self):
        return f'{self.country}'

    class Meta:
        verbose_name_plural = "Country"


class Province(models.Model):
    province = models.CharField(null=True, unique=True, max_length=100)

    def __str__(self):
        return f'{self.province}'

    class Meta:
        verbose_name_plural = "Province"


class District(models.Model):
    district = models.CharField(null=True, unique=True, max_length=100)

    def __str__(self):
        return f'{self.district}'

    class Meta:
        verbose_name_plural = "District"


class Municipality(models.Model):
    municipality = models.CharField(null=True, unique=True, max_length=100)

    def __str__(self):
        return f'{self.municipality}'

    class Meta:
        verbose_name_plural = "Event Municipality"


class Ward(models.Model):
    ward = models.PositiveSmallIntegerField(
        null=True, unique=True)

    def __str__(self):
        return f'{self.ward}'

    class Meta:
        verbose_name_plural = "Ward"


class Skills(models.Model):
    skills = models.CharField(null=True, unique=True, max_length=100)

    def __str__(self):
        return f'{self.skills}'

    class Meta:
        verbose_name_plural = "Skills"
