from category.models import EventCategory
from django.db import models
from customuser.models import User

# Create your models here.


class Events(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(EventCategory, on_delete=models.CASCADE)
    name = models.CharField(max_length=250, null=True)
    posted_at = models.DateTimeField(null=True, auto_now=True)
    location = models.CharField(max_length=100, null=True)
    banner = models.ImageField(default='avatar.jpg', upload_to='Banner_Images')
    start_date = models.DateField(
        auto_now=False, auto_now_add=False, blank=True, null=True)
    end_date = models.DateField(
        auto_now=False, auto_now_add=False, blank=True, null=True)
    description = models.TextField(max_length=2000, null=True)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name_plural = "Events"
