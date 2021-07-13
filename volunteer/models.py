from django.db import models
from django.db.models.base import Model
from customuser.models import User
from events.models import Events
# Create your models here.



class requestevents(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    event=models.ForeignKey(Events,on_delete=models.CASCADE)
    user_details=models.FileField(default='avatar.jpg',upload_to='request_volunteer')
    description=models.TextField(max_length=2000,null=True)
    request_volunteer= models.BooleanField(default=False)
    approved=models.BooleanField(default=False)
    def __str__(self):
        return f'{self.user}'
    

class interestedevents(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    event=models.ForeignKey(Events,on_delete=models.CASCADE)
    interested=models.BooleanField(default=False)
    def __str__(self):
        return f'{self.user}'