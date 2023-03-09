from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from .forms import RegistrationForm
from django.contrib.auth import login, logout, authenticate
from .models import Company
from .models import job

def index(request):
   companies = Company.objects.all()[0:8]
   jobs = job.objects.all()[0:6]
   return render(request,'pages/home.html', {'companies': companies, 'jobs':jobs})

def sign_up(request):
   if request.method == 'POST':
      form = RegistrationForm(request.POST)
      if form.is_valid():
         user = form.save()
         login(request, user)
         return redirect('/')
   else:
      form = RegistrationForm()

   return render(request, 'registration/register.html', {"form": form})

def detail(request, id):
    detail = job.objects.get(id=id)
    return render(request, 'pages/job-detail.html', {'detail': detail})

