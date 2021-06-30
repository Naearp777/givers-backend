from django.db.models.signals import pre_save
from customuser.models import User
def updateUser(sender,instance,**kwargs):
    print("Signals Trigrred")

pre_save.connect(updateUser,sender= User)