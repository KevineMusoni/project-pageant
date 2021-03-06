from django.db import models
from tinymce.models import HTMLField
from django.core.validators import URLValidator
from django.contrib.auth.models import User

# Create your models here.

# user profile class
class Profile(models.Model):
    profile = models.ForeignKey(User,on_delete=models.CASCADE, null = True)
    photo = models.ImageField(upload_to = 'profile/')
    bio = models.TextField(max_length=500)
    def save_profile(self):
        self.save()
    def delete_profile(self):
        self.delete()

# project class
class Project(models.Model):
    title = models.CharField(max_length = 50)
    image = models.ImageField(upload_to = 'projects/')
    description = models.TextField(max_length=1000)
    link=models.TextField(validators=[URLValidator()],null=True)
    profile = models.ForeignKey(User,on_delete=models.CASCADE, null=True)   
    userinterface=models.PositiveIntegerField(choices=list(zip(range(1,11),range(1, 11))), default=1)
    functionality = models.PositiveIntegerField(choices=list(zip(range(1, 11), range(1, 11))), default=1)
    content=models.PositiveIntegerField(choices=list(zip(range(1, 11), range(1, 11))), default=1)

    def save_project(self):
        self.save()
    def delete_project(self):
        self.delete()

    @classmethod
    def get_all(cls):
        projects = cls.objects.all()
        return projects

    @classmethod
    def get_project(cls, project_id):
        project = cls.objects.get(id=project_id)
        return project

    @classmethod
    def search_by_title(cls,search_term):
        projects_title = cls.objects.filter(title__icontains=search_term)
        return projects_title




