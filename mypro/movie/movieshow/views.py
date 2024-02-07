from django.db.models import Q
from django.shortcuts import render
from movieshow.models import movieshow
from django.http import HttpResponse
from movieshow.forms import movieform




# Create your views here.
def home(request):
    v = movieshow.objects.all()
    return render(request, 'home.html',{'mov':v})


def addmovie(request):
    if request.method == 'POST':
        name = request.POST.get('m')
        description = request.POST.get('a')
        year = request.POST.get('p')
        image = request.FILES.get('k')

        # Create a new Movie instance and save it to the database
        mov = movieshow(name=name, description=description, year=year, image=image)
        mov.save()

        # Redirect or return a success response

    return render(request, 'addmovie.html')
def viewmovie(request):
    k = movieshow.objects.all()
    return render(request, 'viewmovie.html', context={'mov': k})
def edit(request,p):
    mov=movieshow.objects.get(id=p)
    if (request.method == "POST"):
        form = movieform(request.POST,request.FILES,instance=mov)
        if form.is_valid():
            form.save()
            return viewmovie(request)
    form=movieform(instance=mov)

    return render(request,'edit.html',{'form':form})

def delete(request,p):
    mov = movieshow.objects.get(id=p)
    mov.delete()
    return viewmovie(request)


