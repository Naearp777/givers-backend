from django.db import models
from customuser.models import User
from notification.models import Notification
from django.db.models.signals import post_save, post_delete

# Create your models here.
class Events(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    name= models.CharField(max_length=250,null=True)
    posted_at=models.DateTimeField(null=True,auto_now=True)
    location=models.CharField(max_length=100,null=True)
    banner=models.ImageField(default='avatar.jpg',upload_to='Banner_Images')
    start_date=models.DateField(auto_now=False,auto_now_add=False,blank=True,null=True)
    end_date=models.DateField(auto_now=False,auto_now_add=False,blank=True,null=True)
    description=models.CharField(max_length=2000,null=True)
    toggle=models.BooleanField(null=True)
    def __str__(self):
        return f'{self.name}'

class Request_as_Volunteer(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    event = models.ForeignKey(Events,on_delete=models.CASCADE)

    def user_requested_volunteer(sender,instance,*args,**kwargs):
        volunteer = instance
        post = volunteer.post
        sender = volunteer.user

        notify  = Notification(post = post,sender = sender,user = post.user, notification_type = 1)
        notify.save()
    
    def user_unrequested_volunteer(sender,instance,*args,**kwargs):
        volunteer = instance
        post = volunteer.post
        sender = volunteer.user

        notify  = Notification.objects.filter(post = post, sender = sender, notification_type = 1)
        notify.delete()

class Interested(models.Model):
    user  = models.ForeignKey(User,on_delete=models.CASCADE)
    event = models.ForeignKey(Events,on_delete=models.CASCADE)

    def user_interested_volunteer(sender,instance,*args,**kwargs):
        volunteer = instance
        post = volunteer.post
        sender = volunteer.user

        notify  = Notification(post = post,sender = sender,user = post.user, notification_type = 1)
        notify.save()


#user_requested_volunteer
post_save.connect(Request_as_Volunteer.user_requested_volunteer,sender =Request_as_Volunteer )
# user_unrequested_volunteer
post_delete.connect(Request_as_Volunteer.user_unrequested_volunteer,sender =Request_as_Volunteer )
#user_requested_volunteer
post_save.connect(Interested.user_interested_volunteer,sender =Interested )


