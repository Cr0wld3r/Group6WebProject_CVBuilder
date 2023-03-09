from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class profile(models.Model):
    postAuthor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='cvs',null=True)
    name = models.CharField(max_length=100)
    major = models.CharField(max_length=100,null=True)
    avatar = models.ImageField(null=True)
    phone = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    year_graduate = models.CharField(max_length=100,null=True)
    degree = models.TextField(max_length=1000)
    university = models.CharField(max_length=100)
    skill = models.TextField(max_length=1000)
    previous_work_title = models.CharField(max_length=100)
    previous_work = models.TextField(max_length=1000)
    previous_work_year = models.CharField(max_length=100,null=True)
    gpa = models.CharField(max_length=5,null=True)
    intro = models.TextField(max_length=1000,null=True)
    address = models.CharField(max_length=100,null=True)

    def __str__(self):
        return self.name