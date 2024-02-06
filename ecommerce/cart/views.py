from django.shortcuts import render
from cart.models import Cart,Account,Order
from shop.models import Products
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

@login_required
def cartview(request):
    total=0
    u=request.user
    try:
        cart=Cart.objects.filter(user=u)
        for i in cart:
            total+=i.quantity*i.products.price
    except:
        pass

    return render(request,'cartview.html',{'c':cart,'total':total})


@login_required
def addcart(request,n):
    p=Products.objects.get(name=n)
    u=request.user
    try:
        cart=Cart.objects.get(user=u,products=p)
        if(p.stock > 0):

            cart.quantity+=1
            cart.save()
            p.stock -= 1
            p.save()
    except:
        if(p.stock > 0):
            cart=Cart.objects.create( products=p,user=u,quantity=1)
            cart.save()
            p.stock-=1
            p.save()

    return cartview(request)

@login_required
def cart_remove(request,n):
    p = Products.objects.get(name=n)
    u = request.user
    try:
        cart = Cart.objects.get(user=u, products=p)
        if (cart.quantity > 1):
            cart.quantity -= 1
            cart.save()
            p.stock+=1
            p.save()
        else:
            cart.delete()
            p.stock += 1
            p.save()
    except:
          pass
    return cartview(request)

@login_required
def full_remove(request,n):
    p = Products.objects.get(name=n)
    u = request.user
    try:
        cart = Cart.objects.get(user=u, products=p)
        cart.delete()
    except:
        pass
    return cartview(request)


@login_required
def orderform(request):
    if request.method=="POST":
        a=request.POST['a']
        p=request.POST['p']
        n=request.POST['n']

        u=request.user
        cart=Cart.objects.filter(user=u)
        total=0
        for i in cart:
            total+=i.quantity*i.products.price
        try:
            num=int(n)
            ac=Account.objects.get(acctnum=n)

            if(ac.amount>=total):
                ac.amount=ac.amount-total
                ac.save()
                for i in cart:
                    o=Order.objects.create(user=u,products=i.products,address=a,phone=p,no_of_items=i.quantity,order_status="paid")
                    o.save()
                cart.delete()
                msg="order placed successfully"
                return render(request,'orderdetail.html',{'msg': msg})
            else:
               msg="cannot place order"
               return render(request, 'orderdetail.html', {'msg': msg})
        except:
            pass
    return render(request, 'orderform.html')

@login_required
def orderview(request):
    u = request.user
    o=Order.objects.filter(user=u)
    return render(request,'orderview.html',{'o':o,'u':u.username})