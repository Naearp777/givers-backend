from events.models import Events
from django.db import models
from customuser.models import User
# Create your models here.


class Invitation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    event = models.ForeignKey(Events, on_delete=models.CASCADE)
    description = models.TextField(max_length=2000, blank=True, null=True)
    read = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return f'{self.user}--{self.event}'

    class Meta:
        verbose_name_plural = "Invitation"
