from shop.models import Products
from django.shortcuts import render
from django.db.models import Q
def search(request):
    query = ""
    product= None

    if(request.method == "POST"):

        query = request.POST['q']

        product = Products.objects.filter(Q(name__icontains=query) | Q(desc__icontains=query))
    return render(request,'search.html',{'query':query,'p':product})
