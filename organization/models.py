from django.db import models
from events.models import Events
# Create your models here.


class requestform(models.Model):
    event = models.ForeignKey(Events, on_delete=models.CASCADE)
    ques_1 = models.TextField(max_length=2000, null=True)
    ques_2 = models.TextField(max_length=2000, null=True)
    ques_3 = models.TextField(max_length=2000, null=True)
    file_1 = models.TextField(max_length=2000, null=True)

    def __str__(self):
        return f'{self.event}'

    class Meta:
        verbose_name_plural = "Request Form"
