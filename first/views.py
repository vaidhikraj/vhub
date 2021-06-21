from django.shortcuts import render,redirect,get_object_or_404
from . import views
# Create your views here.
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.models import User
from django.db import IntegrityError
from .models import BlogTable
from .forms import BlogForm
from django.contrib.auth.decorators import login_required


def index(request):
    a=BlogTable.objects.filter(public=True).order_by('-today')
    global post
    post=len(a)

    return render(request,'tempfirst/index.html',{'data':a,'post':post})

def signup(request):
    if request.method=='POST':
        if request.POST['password1']==request.POST['password2']:
            try:
                u=User.objects.create_user(username=request.POST['username'],password=request.POST['password1'])
                u.save()
                return redirect('ulogin')
            except IntegrityError:
                return render(request,'tempfirst/signup.html')
            
    return render(request,'tempfirst/signup.html',{'post':post})

def botist(request):
    return render(request,'tempfirst/botist.html')

def ulogin(request):
    if request.method=='POST':
        a=authenticate(request,username=request.POST['username'],password=request.POST['password'])
        if a is not None:
            login(request,a)
            return redirect('home')
        else:
            return render(request,'tempfirst/ulogin.html')

    return render(request,'tempfirst/ulogin.html',{'post':post})


@login_required(login_url="ulogin")
def home(request):
    if request.method=='GET':
        a=BlogTable.objects.filter(public=True).order_by('-today')
        return render(request,'tempfirst/home.html',{'data':a,'post':post})

@login_required(login_url="ulogin")
def blog(request):
    if request.method=='POST':
        a=BlogForm(request.POST,request.FILES)
        
        b=a.save(commit=False)
        b.user=request.user
        b.save()
        print(b.foto.url)
        return redirect('home')
        
    return render(request,'tempfirst/blog.html',{'form':BlogForm(),'post':post})

@login_required(login_url="ulogin")
def myblog(request):
    b=BlogTable.objects.filter(user=request.user).order_by('-today')
    return render(request,'tempfirst/myblog.html',{'data':b,'post':post})
    
@login_required(login_url="ulogin")
def status(request):
    b=BlogTable.objects.filter(user=request.user)
    return render(request,'tempfirst/status.html',{'data':b,'post':post})


@login_required(login_url="ulogin")
def viewblog(request,id):
    g=get_object_or_404(BlogTable,pk=id,user=request.user)
    f=BlogForm(instance=g)
    if request.method=='POST':
        a=BlogForm(request.POST,request.FILES,instance=g)

        a.save()
        return redirect('home')


    return render(request,'tempfirst/viewblog.html',{'form':f,'post':post})



@login_required(login_url="ulogin")
def delete(request,id):
    d=get_object_or_404(BlogTable,pk=id,user=request.user)
    if request.method=='GET':
        d.delete()
        return redirect('myblog')
    
        


@login_required(login_url="ulogin")
def ulogout(request):
    if request.method=='GET':
        logout(request)
        return redirect('index')