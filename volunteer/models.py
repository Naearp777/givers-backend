from django.db import models
from customuser.models import User
from events.models import Events
# Create your models here.


class requestevents(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    event = models.ForeignKey(Events, on_delete=models.CASCADE)
    user_details = models.FileField(
        default='avatar.jpg', upload_to='request_volunteer')
    ques_1 = models.TextField(max_length=2000, null=True)
    ques_2 = models.TextField(max_length=2000, null=True)
    ques_3 = models.TextField(max_length=2000, null=True)
    ans_1 = models.TextField(max_length=2000, null=True)
    ans_2 = models.TextField(max_length=2000, null=True)
    ans_3 = models.TextField(max_length=2000, null=True)
    file_1 = models.TextField(max_length=200, null=True)
    # description=models.TextField(max_length=2000,null=True)
    request_volunteer = models.BooleanField(default=False)
    approved = models.BooleanField(default=False)
    pending = models.BooleanField(default=True)
    task_assigned = models.TextField(max_length=2000, null=True,blank=True)

    def __str__(self):
        return f'{self.user}'

    class Meta:
        verbose_name_plural = "Request Event"


class interestedevents(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    event = models.ForeignKey(Events, on_delete=models.CASCADE)
    interested = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.user}'

    class Meta:
        verbose_name_plural = "Interested Event"
