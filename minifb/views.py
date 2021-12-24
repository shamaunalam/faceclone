from django.shortcuts import render,redirect
from .models import UserProfile,UserPost

from django.contrib.auth import authenticate,login,logout

from django.contrib.auth.decorators import login_required

from django.contrib.auth.models import User

# Create your views here.
def index(request):
    if request.user.is_anonymous:

        if request.method=='POST':

            username = request.POST['username']
            password = request.POST['password']

            user = authenticate(username=username,password=password)

            if user.is_authenticated:
                login(request,user)
                return redirect('home')
            else:
                return redirect('login')
        else:
            return render(request,'index.html')
    else:
        return redirect('home')


@login_required(login_url='login')
def home(request):
    pro = UserProfile.objects.get(user=request.user)
    pos = UserPost.objects.filter(user=request.user)
    context={'pro':pro,'pos':pos}
    
    return render(request,'home.html',context)



@login_required(login_url='login')
def profile(request):
    if not request.user.is_anonymous:
        user = request.user
        pro = UserProfile.objects.get(user=user)
        context = {'pro':pro}
    return render(request,'profile.html',context)

@login_required(login_url='login')
def edit_profile(request):
    if request.method=='POST':
        status = request.POST['status']
        loc = request.POST['location']

        pro = UserProfile.objects.get(user=request.user)
        pro.status = status
        pro.location = loc
        pro.save()
        return redirect('profile')

def Logout(request):
    logout(request)
    return redirect('login')

def register(request):
    if request.method=='POST':
        username = request.POST['username']
        password = request.POST['password']
        user = User.objects.create(username=username)
        user.set_password(password)
        user.save()
        pro = UserProfile.objects.create(user=user)
        pro.save()
        return redirect('login')


def create_post(request):
     if request.method=='POST':
         content = request.POST['content']

         pos = UserPost.objects.create(user=request.user,content=content)
         pos.save()
         return redirect('home')