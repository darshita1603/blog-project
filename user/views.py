from django import forms
from django.http import request
from django.shortcuts import redirect, render
from django.contrib import messages
# from django.contrib.auth.forms import UserCreationForm
from .forms import UserRegisterForm


# Create your views here.
def register(request):
    # print(request,"ggggg")
    # form= UserRegistrationForm()
    if request.method=='POST':
        # print(request.method,"ffff")
        form=UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data.get('username')
            messages.success(request,f'Account created for {username}')
            return redirect('blog-home')
        
    else:
        form = UserRegisterForm()
    return render(request,'users/registration.html',{'form':form})

def profile(request):
    return render(request,'users/profile.html')
