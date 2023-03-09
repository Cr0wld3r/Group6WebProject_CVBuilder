from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
   # path('', views.index),
   path('', views.index, name='home'),
   path('register/', views.sign_up, name='sign-up'),
   path('job-detail/<int:id>', views.detail),
]