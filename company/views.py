from django.shortcuts import render
from home.models import Company
# Create your views here.

def index(request):
   companies = Company.objects.all()[0:8]
   return render(request,'pages/company.html', {'companies': companies})
def detail(request, id):
    detail = Company.objects.get(id=id)
    return render(request, 'pages/company-detail.html', {'detail': detail})