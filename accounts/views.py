from django.shortcuts import render
from .models import UserPost
from django.views.generic import ListView, DetailView
from .models import Profile

# Create your views here.
def dashboard(request):
    return render(request, 'profile_list.html')

def profile_list(request):
    profiles = Profile.objects.exclude(user=request.user)
    return render(request, "profile_list.html", {"profiles": profiles})

def profile(request, pk):
    profile = Profile.objects.get(pk=pk)
    return render(request, "profile.html", {"profile": profile})

