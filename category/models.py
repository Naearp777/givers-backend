from django.db import models

# Create your models here.


class EventCategory(models.Model):
    category = models.CharField(null=True, unique=True, max_length=100)

    def __str__(self):
        return f'{self.category}'

    class Meta:
        verbose_name_plural = "Event categories"


class Skills(models.Model):
    skills = models.CharField(null=True, unique=True, max_length=100)

    def __str__(self):
        return f'{self.skills}'

    class Meta:
        verbose_name_plural = "Skills"
