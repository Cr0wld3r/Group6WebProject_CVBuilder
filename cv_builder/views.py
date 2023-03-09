from django.shortcuts import render
from .models import profile
from .forms import ProfileForm
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required

# Create your views here.
# def cv_builder(request):
#     if request.method=="POST":
#         cvForm = ProfileForm(request.POST, request.FILES)
#         if cvForm.is_valid():
#                 profile = cvForm.save()
#                 profile.owner = request.user.id
#                 profile.save()
#                 return HttpResponseRedirect("/")
#     else:
#       cvForm = ProfileForm()
#     return render(request,"pages/cv_builder.html",{"cvForm": cvForm})

@login_required(login_url="/login")
def cv_builder(request):
    if request.method=="POST":            
            name = request.POST.get("name","")
            major = request.POST.get("major","")
            avatar = request.FILES.get("avatar","")
            phone = request.POST.get("phone","")
            email = request.POST.get("email","")
            year_graduate = request.POST.get("year_graduate","")
            degree = request.POST.get("degree","")
            university = request.POST.get("university","")
            skill = request.POST.get("skill","")
            previous_work_title = request.POST.get("previous_work_title","")
            previous_work = request.POST.get("previous_work","")
            previous_work_year = request.POST.get("previous_work_year","")
            gpa = request.POST.get("gpa","")
            intro = request.POST.get("intro","")
            address = request.POST.get("address","")

            Profile=profile(address = address, name=name,major=major, year_graduate = year_graduate, previous_work_title = previous_work_title, previous_work_year = previous_work_year, gpa = gpa, intro = intro, phone=phone,email=email,degree=degree,university=university,skill=skill,previous_work=previous_work,avatar=avatar)
            Profile.postAuthor = request.user
            Profile.save()
            return HttpResponseRedirect("/cv_builder/list")

    return render(request,"pages/cv_builder.html")

@login_required(login_url="/login")
def list(request):
    Profile=profile.objects.all()
    # current_user = request.user
    return render(request,"pages/cv_list.html",{'profile':Profile})

@login_required(login_url="/login")
def reviewResume(request, id):
    user_profile=profile.objects.get(pk=id)

    if request.method == "POST":
        user_profile = request.POST.get("user_profile")
        cv =  profile.objects.filter(id=user_profile).first()
        if cv and cv.postAuthor == request.user:
            cv.delete()
            return HttpResponseRedirect("/cv_builder/list")

    return render(request,"pages/cv_review.html",{'user_profile':user_profile})