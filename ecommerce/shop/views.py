from django.shortcuts import render
from shop.models import Category,Products
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponse

def allcategories(request):
    c=Category.objects.all()
    return render(request,'category.html',{'c':c})

def allproducts(request,p):
    c =Category.objects.get(name=p)
    p= Products.objects.filter(category=c)
    return render(request,'products.html', {'c':c,'p':p})


def detail(request,p):
    p =Products.objects.get(name=p)
    return render(request,'detail.html', {'p':p})

def register(request):

        if (request.method== "POST"):
            u = request.POST['u']
            p = request.POST['p']
            cp = request.POST['cp']
            e = request.POST['e']
            f = request.POST['f']
            l = request.POST['l']

            if (p == cp):
                user = User.objects.create_user(username=u, password=p, email=e, first_name=f, last_name=l)
                user.save()
                return redirect('shop:allcat')
            else:
                return HttpResponse("passwords are not same")
        return render(request, 'register.html')

def userlogin(request):
    if (request.method=="POST"):
        u=request.POST['u']
        p=request.POST['p']
        user=authenticate(username=u,password=p)
        if user:
            login(request,user)
            return redirect('shop:allcat')
        else:
            return  HttpResponse("invalid credential")
    return render(request,'userlogin.html')


def userlogout(request):
    logout(request)
    return redirect('shop:userlogin')


