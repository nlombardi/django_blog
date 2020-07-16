from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile

"""
 When the user is saved then send the signal which is received by the receiver
 which then takes the function create_profile with the arguements, if the user is created
 then take all the arguements and pass to the Profile class from the objects of the user that is created.
"""
@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_profile(sender, instance, created, **kwargs):
    instance.profile.save()