from django.shortcuts import render,redirect
from django.http  import HttpResponse,Http404
from .models import Project,Profile
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required
from .forms import ProfileForm,ProjectForm,VoteForm
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializer import ProjectSerializer, ProfileSerializer

# Create your views here.
@login_required(login_url='/accounts/login/')
def index(request):
    current_user = request.user
    projects = Project.get_all()
    return render(request,'index.html',{'projects':projects})
    
def project(request,project_id):
    project = Project.objects.get(id = project_id)
    rating = round(((project.userinterface + project.functionality )/2),2)
    if request.method == 'POST':
        form = VoteForm(request.POST)
        if form.is_valid:
            if project.userinterface == 1:
                project.userinterface = int(request.POST['userinterface'])
            else:
                project.userinterface = (project.userinterface + int(request.POST['userinterface']))/2
            if project.functionality == 1:
                project.functionality = int(request.POST['functionality'])
            else:
                project.functionality = (project.userinterface + int(request.POST['functionality']))/2
    else:
        form = VoteForm()
    return render(request,'project.html',{'form':form,'project':project,'rating':rating})

@login_required(login_url='/accounts/login/')
def new_project(request):
    current_user = request.user
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            project = form.save(commit=False)
            project.profile = current_user
            project.save()
        return redirect('indexPage')

    else:
        form = ProjectForm()
    return render(request, 'new_project.html', {"form": form})

def vote_project(request, project_id):
    project = Project.objects.get(id=project_id)
    rating = round(((project.userinterface + project.functionality)/2),2)
    if request.method == 'POST':
        form = VoteForm(request.POST)
        if form.is_valid:
            if project.userinterface == 1:
                project.userinterface = int(request.POST['userinterface'])
            else:
                project.userinterface = (project.userinterface + int(request.POST['userinterface']))/2
            if project.functionality == 1:
                project.functionality = int(request.POST['functionality'])
            else:
                project.functionality = (project.userinterface + int(request.POST['functionality']))/2
    else:
        form = VoteForm()
    return render(request,'vote.html',{'form':form,'project':project,'rating':rating})


def profile(request):
    current_user = request.user
    projects = Project.objects.filter(profile=current_user).all()
    profile = Profile.objects.filter(profile=current_user)

    if len(profile)<1:
        profile = "No profile"
    else:
        profile = Profile.objects.get(profile=current_user)

    return render(request, 'profile.html',{'projects':projects,'profile':profile})

def edit_profile(request):
    current_user = request.user
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            profile = form.save(commit = False)
            profile.project = current_user
            profile.save()
        return redirect('Profile')
    else:
        form = ProfileForm()
    return render(request,'edit_profile.html',{'form':form})

def search_results(request):

    if 'project' in request.GET and request.GET["project"]:
        search_term = request.GET.get("project")
        searched_projects = Project.search_by_title(search_term)
        message = f"{search_term}"

        return render(request, 'search.html',{"message":message,"projects": searched_projects})

    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html',{"message":message})

def search_project(request,project_id):
    try :
        project = Project.objects.get(id = project_id)

    except ObjectDoesNotExist:
        raise Http404()
    return render(request, 'project_details.html', {'project':project})

class ProjectList(APIView):
    def get(self, request, format=None):
        all_project =Project.objects.all()
        serializers = ProjectSerializer(all_project, many=True)
        return Response(serializers.data)

class ProfileList(APIView):
    def get(self, request, format=None):
        all_profile =Profile.objects.all()
        serializers = ProfileSerializer(all_profile, many=True)
        return Response(serializers.data)