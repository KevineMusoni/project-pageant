from django.db import models
from tinymce.models import HTMLField

# Create your models here.
class Profile(models.Model):
    photo = models.ImageField(upload_to = 'profile/')
    Profile = models.ForeignKey(User,on_delete=models.CASCADE, null = True)
    bio = models.TextField(max_length=500)

    def save_profile(self)
        self.save()
    def delete_profile(self)
        self.delete()
