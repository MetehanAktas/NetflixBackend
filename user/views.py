from django.shortcuts import render,redirect
from .forms import *
from django.contrib.auth import authenticate,login,logout
from .models import *
from django.contrib import messages
# Create your views here.

def UserRegister(request):
    if request.method == "POST":
        isim = request.POST["isim"]
        soyisim = request.POST["soyisim"]
        email = request.POST["email"]
        tel = request.POST["tel"]
        dogum = request.POST["dogum"]
        sifre1 = request.POST["sifre1"]
        sifre2 = request.POST["sifre2"]
        if sifre1 == sifre2:
            if User.objects.filter(email=email).exists():
                messages.error(request,"Bu e-mail zaten kullanımda")
                return redirect("register")
            elif len(sifre1)<6:
                messages.error(request,"Şifre en az 6 karakter olmalı")
            else:
                user = User.objects.create_user(username=email,email=email,password=sifre1)
                Kullanici.objects.create(
                    user = user,
                    isim = isim,
                    soyisim = soyisim,
                    email = email,
                    tel = tel,
                    dogum = dogum,
                )
                user.save()
                messages.success(request,"Kullanıcı Oluşturuldu")
                return redirect("login")
    return render(request,"register.html")

def UserLogin(request):
    if request.method == 'POST':
        username=request.POST["username"]
        password=request.POST["password"]
        
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect("browse-index")
    return render(request,"login.html")

def UserLogout(request):
    logout(request)
    return redirect("index")

def profiles(request):
    profiller = Profile.objects.filter(owner= request.user)
    context={
        "profiller":profiller
    }
    return render(request,"browse.html",context)


def createProfile(request):
    form = ProfileForm()
    if request.method == "POST":
        form = ProfileForm(request.POST,request.FILES)
        if form.is_valid():
            profiles= form.save(commit=False)
            profiles.owner = request.user
            profiles.save()
            return redirect("profil")
    context = {
        "form":form,
    }
    return render(request,"create.html",context)

def hesap(request):
    user = Kullanici.objects.get(id=6)
    context={
        "user":user
    }
    return render(request,"hesap.html",context)

def userDelete(request):
    user = request.user
    user.delete()
    messages.success(request,"Hesabınız Silindi")
    return redirect("index")