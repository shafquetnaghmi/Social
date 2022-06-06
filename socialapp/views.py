from django.shortcuts import render
from django.http import HttpResponse
from .forms import LoginForm,UserRegistrationForm,UserEditForm,ProfileEditForm,ImageForm
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect 
from .models import Profile,Image
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages

def user_login(request):
    form=LoginForm()
    if request.method=="POST":
        form=LoginForm(request.POST)
        if form.is_valid():
            cd=form.cleaned_data
            user=authenticate(request,username=cd['username'],password=cd['password'])
            if user is not None:
                if user.is_active:
                   login(request,user)
                   return redirect('/dashboard/')
                else:
                   return HttpResponse('Disabled account')
            else:
                return HttpResponse('invalid account')
    else:
           form=LoginForm()
    context={'form':form}
    return render(request,'socialapp/user_login.html',context)
def user_logout(request):
     logout(request)
     return render(request,'socialapp/user_logout.html')
     #messages.success(request,'You have been logged out ')
@login_required()
def dashboard(request):
    posts=Image.objects.filter(user__profile__followers=request.user.id)
    context={'posts':posts}
    return render(request,'socialapp/dashboard.html',context)

def UserRegistration(request):
    form=UserRegistrationForm()
    if request.method=='POST':
        form=UserRegistrationForm(request.POST)
        if form.is_valid():
            new_user=form.save(commit=False)
            new_user.set_password(form.cleaned_data['password1'])
            new_user.save()
            Profile.objects.create(user=new_user)
            #return HttpResponse(f'Welcome {new_user.first_name} \n Accounted created successfully')
            #return redirect('/register_done/')
            return render(request,'registration/register_done.html',{'new_user': new_user})

            
    else:
        form=UserRegistrationForm()
    context={'form':form,}
    return render(request,'registration/UserRegistration.html',context)

def registerdone(request):
    return render(request,'registration/register_done.html')

def user_profile(request,username):
    #profile=Profile.objects.filter(user_id=1)  #Tried both given below line didn't workout 
    #user=User.objects.filter(id=1)
    user = get_object_or_404(User, username=username)
    profile = get_object_or_404(Profile, user=user)
    follower_count=profile.followers.count()
    following_count=profile.following.count()
    #photos uploaded 
    user=get_object_or_404(User,username=username)
    img=user.images_created.all()
    

    context={'profile':profile,'user':user,'img':img,'follower_count':follower_count,'following_count':following_count}
    return render(request,'socialapp/user_profile.html',context)

#def user_profile(request,pk):                #both the above method work  
    #profile=Profile.objects.filter(user_id=1)
    #user=User.objects.filter(id=1)
    #user = get_object_or_404(User, id=pk)
    #profile = get_object_or_404(Profile, user_id=pk)
    #context={'profile':profile,'user':user,}
    #return render(request,'socialapp/user_profile.html',context)
@login_required
def editprofile(request):
    user_form=UserEditForm(instance=request.user)
    profile_form=ProfileEditForm(instance=request.user.profile)
    if request.method=='POST':
       user_form=UserEditForm(data=request.POST,instance=request.user)
       profile_form=ProfileEditForm(data=request.POST,instance=request.user.profile,files=request.FILES)
       if user_form.is_valid() and profile_form.is_valid() :
         user_form.save()
         profile_form.save()
         #return HttpResponse('profile saved')
         messages.success(request, 'Profile updated successfully') 
       else:
         messages.error(request, 'Error updating your profile')
    context={'user_form':user_form,'profile_form':profile_form}
    return render(request,'socialapp/editprofile.html',context)

@login_required
def imageview(request):
    form=ImageForm()
    
    if request.method=='POST':
        form=ImageForm(request.POST,files=request.FILES)
        if form.is_valid():
            #cd=form.cleaned_data
            new_form=form.save(commit=False)
            new_form.user=request.user
            new_form.save()
            return HttpResponse('form submitted successfully')
        else:
            return HttpResponse('invalid form')
    context={'form':form}
    return render(request,'socialapp/image.html',context)


def image_on_dashboard(request,username): #not using this one 
    #img=get_object_or_404(Image,pk=user_id)
    user=get_object_or_404(User,username=username)
    img=user.images_created.all()
    context={'img':img}
    return render(request,'socialapp/image_on_dashboard.html',context)
    
def search(request):
    search=request.GET['username']
    profiles=Profile.objects.filter(user__username__icontains=search)
    #profile = get_object_or_404(Profile, id=user_id)
    #follower_count=profile.followers.count()
    #following_count=profile.following.count()
    context={'profiles':profiles,}
    return render(request,'socialapp/search.html',context)

def follow(request,id,username):
    profile=Profile.objects.get(id=id)    
    profile.followers.add(request.user)    #adding followers to request.user
    login_profile=Profile.objects.get(user=request.user)
    login_profile.following.add(profile.user)           #adding following to searched profile
    #return redirect(f'/search/?username={username}')
    return redirect(f'/profile/{username}')
    
def unfollow(request,id,username):
    profile=Profile.objects.get(id=id)
    profile.followers.remove(request.user)
    login_profile=Profile.objects.get(user=request.user)
    login_profile.following.remove(profile.user)
    return redirect(f'/profile/{username}')

def users_like(request,id,username):
    image=get_object_or_404(Image,id=4)
    image.users_like.add(request.user)
    return redirect('/dashboard/')