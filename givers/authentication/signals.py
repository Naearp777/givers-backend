from django.db.models.signals import pre_save
from customuser.models import User
def updateUser(sender,instance,**kwargs):
    #user  = instance.volunteer
    if instance.email != '':
        instance.full_name = instance.email


pre_save.connect(updateUser,sender= User)