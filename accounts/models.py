from django.contrib.auth.models import User
from django.db import models

# from PIL import Image


class UserProfileManager(models.Manager):
    def get_queryset(self):
        return super(UserProfileManager, self).get_queryset().filter(city="Berlin")

class UserProfile(models.Model):
    user = models.OneToOneField(User,models.CASCADE)
    description = models.TextField(max_length=140, null=True, blank=True)
    city = models.CharField(max_length=100, null=True, blank=True)
    website = models.URLField(default="",null=True, blank=True)
    phone = models.CharField(max_length=17, null=True, blank=True)
    image = models.ImageField(
        default="default.svg",
        upload_to="profile_image",
        blank=True)

    def __str__(self):
        return f"{self.user.username}'s Profile"

# TODO: Find another way to resize to big user profile images
    # def save(self):
    #     super().save()
    #     print("\n HIER",Image.open(self.image),"\n")
    #     img = Image.open(self.image.path)
    #     if img.height > 300 or img.width > 300:
    #         output_size = (300, 300)
    #         img.thumbnail(output_size)
    #         img.save(self.image.path)

    class Meta:
        managed = True
        db_table = 'user_profiles'
