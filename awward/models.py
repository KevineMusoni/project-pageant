from django.db import models
from tinymce.models import HTMLField
from django.core.validators import URLValidator
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    photo = models.ImageField(upload_to = 'profile/')
    Profile = models.ForeignKey(User,on_delete=models.CASCADE, null = True)
    bio = models.TextField(max_length=500)

    def save_profile(self)
        self.save()
    def delete_profile(self)
        self.delete()

class Projects(models.Model):
    title = models.CharField(max_length = 50)
    image = models.ImageField(upload_to = 'projects/')
    description = models.TextField(max_length=1000)
    link=models.TextField
    (validators=[URLValidator(),null= True])
    profile = models.ForeignKey(User,on_delete=models.CASCADE, null=True)   
    userinterface=models.PositiveIntegerField(choices=list(zip(range(1,11),range(1, 11))), default=1)
    functionality = models.PositiveIntegerField(choices=list(zip(range(1, 11), range(1, 11))), default=1)
    
    def save_projects(self):
        self.save()






