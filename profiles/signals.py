from django.db.models.signals import post_save, pre_delete
from django.contrib.auth.models import User
from django.dispatch import receiver
from account.models import ProfileModel
 
 
@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        ProfileModel.objects.create(user=instance)
  
@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
        instance.ProfileModel.save()