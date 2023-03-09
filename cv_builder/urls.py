from django.urls import path
from . import views

urlpatterns = [
  path('', views.cv_builder),
  path('list',views.list),
  path('<int:id>',views.reviewResume),
]