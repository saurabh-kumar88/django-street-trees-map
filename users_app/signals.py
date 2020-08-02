# from django.db.models.signals import post_save
# from django.contrib.auth.models import User
# from django.dispatch import receiver
# from .models import Profile

# # run every time a new user is created
# # sender is a User, which will trigger the signal post_save --> and this signal will received by @receiver() which is our create_profile method.

# @receiver(post_save, sender=User)
# def create_profile(sender, instance, created, **kwargs):
#   if created:
#     Profile.objects.create(user=instance)

# @receiver(post_save, sender=User)
# def save_profile(sender, instance, created, **kwargs):
#   instance.profile.save()

