from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.urls import reverse


# Create your models here.

class Comment(models.Model):
    commenter=models.ForeignKey(User, on_delete=models.CASCADE)
    comment=models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return f"{self.comment[:10]} by {self.commenter.username}"

class Like(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.username}"

class UserPost(models.Model):
    source=models.FileField(upload_to='media')
    desc=models.TextField(max_length=300, null=True, blank=True)
    created_date=models.DateField(auto_now_add=True)
    comment=models.ForeignKey(Comment, on_delete=models.CASCADE, null=True, blank=True)
    like=models.ForeignKey(Like, on_delete=models.CASCADE, null=True, blank=True)

class Profile(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    dob=models.DateField(auto_now_add=True, blank=True, null=True)
    status=models.CharField(max_length=200, blank=True, null=True)
    follows=models.ManyToManyField('self', related_name='followed_by', symmetrical=False, blank=True)
    post=models.ForeignKey(UserPost, on_delete=models.DO_NOTHING, null=True, blank=True)

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        user_profile = Profile(user=instance)
        user_profile.save()
        user_profile.follows.add(instance.profile)
        user_profile.save()

def get_absolute_url(self):
    return reverse('prof_list',args=[str(self.id)])




