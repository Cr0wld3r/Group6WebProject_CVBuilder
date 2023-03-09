import re
from django import forms
from .models import profile
from django.forms import ModelForm


class ProfileForm(forms.Form):
    name = forms.CharField(label='Họ tên', max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Họ và tên'}))
    major = forms.CharField(label='Chuyên ngành', max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Chuyên ngành'}))
    email = forms.EmailField(label='Email',widget=forms.TextInput(attrs={'placeholder': 'Email'}))
    phone = forms.CharField(label='SĐT', max_length=100, widget=forms.TextInput(attrs={'placeholder': '08-xxxxxxxxxxx'}))
    year_graduate = forms.CharField(label='Năm nhập học', max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Năm nhập học'}))
    degree = forms.CharField(label='Ngành học', max_length=100, widget=forms.Textarea())
    university = forms.CharField(label='Trường học', max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Trường học'}))
    intro = forms.CharField(label='Giới thiệu', max_length=100, widget=forms.Textarea(attrs={'placeholder': 'Giới thiệu'}))
    gpa = forms.CharField(label='GPA', max_length=10, widget=forms.TextInput(attrs={'placeholder': 'GPA:x.x'}))
    skill = forms.CharField(label='Skill', max_length=100, widget=forms.Textarea(attrs={'placeholder': 'HTML, CSS, Javascript,...'}))
    previous_work_title = forms.CharField(label='Vị trí từng làm', max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Vị trí từng làm'}))
    previous_work = forms.CharField(label='Mô tả vị trí', max_length=1000, widget=forms.Textarea(attrs={'placeholder': 'Mô tả vị trí'}))
    previous_work_year = forms.CharField(label='Thời gian tham gia', max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Thời gian tham gia'}))
    avatar = forms.ImageField()