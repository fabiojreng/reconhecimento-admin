from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import User
from .utils import send_message_queue


@receiver(post_save, sender=User)
def notify_new_user(sender, instance, created, **kwargs):
    print(instance.photo.url)
    if created:
        send_message_queue(instance)
