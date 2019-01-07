from django import forms
from .models import Profile, Project

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        exclude = ['profile','functionality','userinterface','content']

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['profile']
class VoteForm(forms.ModelForm):
    class Meta:
        model = Project
        exclude = ['link','description','profile','image','title']     