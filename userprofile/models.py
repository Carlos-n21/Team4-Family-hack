from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='profile_pics', blank=True, null=True)

    def __str__(self):
        return f'{self.user.username} Profile'

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    # Check if profile exists before trying to save it
    if hasattr(instance, 'profile'):
        instance.profile.save()

class GuideBookmark(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    device_type = models.CharField(max_length=30)
    guide_type = models.CharField(max_length=20)
    guide_key = models.CharField(max_length=64)

    class Meta:
        unique_together = ('user', 'device_type', 'guide_type', 'guide_key')