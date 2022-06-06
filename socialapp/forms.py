from django import forms 
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm,TextInput,EmailInput,PasswordInput,Textarea,FileInput
from .models import Profile,Image


class LoginForm(forms.Form):
    username=forms.CharField(max_length=50,widget=forms.TextInput(attrs={'placeholder':'Username or Email'}))
    password=forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'password'}))

class UserRegistrationForm(UserCreationForm):
    email=forms.EmailField(max_length=50,help_text='Required',widget=forms.EmailInput(attrs={'placeholder':'email'}))
    password1=forms.CharField(max_length=50,widget=forms.PasswordInput(attrs={'placeholder':'password'}))
    password2=forms.CharField(max_length=50,widget=forms.PasswordInput(attrs={'placeholder':'Re Enter password'}))
    
    class Meta:
        model=User
        fields=['username','email','password1','password2','first_name','last_name']
        widgets={
            'username':TextInput(attrs={'placeholder':'username'}),
            'first_name':TextInput(attrs={'placeholder':'First Name'}),
            'last_name':TextInput(attrs={'placeholder':'Last Name'}),
        }

class UserEditForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['first_name','last_name','email']

class ProfileEditForm(forms.ModelForm):
    class Meta:
        model=Profile
        fields=['date_of_birth','photo']

class ImageForm(forms.ModelForm):
    class Meta:
        model=Image
        fields=['image','description']
        widgets={
            'image':FileInput(attrs={'placeholder':'share photos and videes'}),
        
            'description':TextInput(attrs={'placeholder':'Write a caption'}),
        }