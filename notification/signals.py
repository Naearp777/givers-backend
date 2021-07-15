from django.db.models.signals import post_save
from notifications.signals import notify
from events.models import Events

def my_handler(sender, instance, created, **kwargs):
    notify.send(instance, verb='event was saved')


post_save.connect(my_handler, sender=Events)