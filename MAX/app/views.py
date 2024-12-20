from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from .models import *
import os
from django.contrib.auth.models import User
from django.contrib import messages
# Create your views here.

from django.core.mail import send_mail
from django.conf import settings


def shop_login(req):
    if 'shop' in req.session:
        return redirect(shop_home)
    if 'user' in req.session:
        return redirect(user_home)
    else:
    
        if req.method=='POST':
            uname=req.POST['uname']
            password=req.POST['password']
            data=authenticate(username=uname,password=password)
            if data:
                login(req,data)
                if data.is_superuser:
                    req.session['shop']=uname      # create
                    return redirect(shop_home)
                else:
                    req.session['user']=uname      # create
                    return redirect(user_home)
            else:
                messages.warning(req,"invalid uname or password")  
        return render(req,'login.html') 

def shop_logout(req):
    logout(req)
    req.session.flush()             # delete 
    return redirect(shop_login) 

def  register(req):
     if req.method=='POST':
        name=req.POST['name']       
        email=req.POST['email']
        password=req.POST['password']
        send_mail('Eshop registration', 'E_shop account created', settings.EMAIL_HOST_USER, [email])

        try:
            data=User.objects.create_user(first_name=name,username=email,email=email,password=password)
            data.save()
            return redirect(shop_login)
        except:
            messages.warning(req,"user details already exits")
            return redirect(register)
     else:
         return render(req,'register.html')
          

#--------------------- admin-------------------------------------------------------------------------------------------  

def shop_home(req):
    if 'shop' in req.session:
        Product=product.objects.all()
        return render(req,'shop/shop_home.html',{'products':Product})
    else:
        return redirect(shop_login)  


def add_product(req):
    if req.method=='POST':
        id=req.POST['pro_id']
        name=req.POST['name']       
        price=req.POST['price']       
        offer_price=req.POST['offer_price']       
        file=req.FILES['img']
        data=product.objects.create(pro_id=id,name=name,price=price,offer_price=offer_price,img=file)   
        data.save()
        return redirect(shop_home)
    return render(req,'shop/add_pro.html') 


def edit_pro(req,id):
        pro=product.objects.get(pk=id)
        if req.method=='POST':
            m_id=req.POST['pro_id']
            name=req.POST['name']       
            price=req.POST['price']       
            offer_price=req.POST['offer_price']       
            file=req.FILES['img']
            print(file)
            if file:
                product.objects.filter(pk=id).update(pro_id=m_id,name=name,price=price,offer_price=offer_price,img=file)   
            else:
                product.objects.filter(pk=id).update(pro_id=m_id,name=name,price=price,offer_price=offer_price)   

            return redirect(shop_home)
        return render(req,'shop/edit_pro.html',{'data':pro}) 


def delete_pro(req,id):
        data=product.objects.get(pk=id)
        url=data.img.url
        url=url.split('/')[-1]
        os.remove('media/'+url)  
        data.delete()
        return redirect(shop_home) 


def bookings(req):
    bookings=Buy.objects.all()[::-1][:10]
    return render(req,'shop/bookings.html',{'data':bookings})


#------------------------------------- User--------------------------------------------------------------

def user_home(req):
    if 'user' in req.session:
        Product=product.objects.all()
        return render(req,'user/user_home.html',{'products':Product})                  
    

def view_product(req,id):
     user=User.objects.get(username=req.session['user'])
     Product=product.objects.get(pk=id)
     try:
         cart=Cart.objects.get(product=Product,user=user)
     except:
         cart=None    
     return render(req,'user/view_pro.html',{'products':Product,'cart':cart})                  


def add_to_cart(req,id):
     Product=product.objects.get(pk=id)
     print(Product)
     user=User.objects.get(username=req.session['user'])
     print(user)
     data=Cart.objects.create(user=user,product=Product)
     data.save()
     return redirect(cart_display)


def cart_display(req):
    user=User.objects.get(username=req.session['user'])
    data=Cart.objects.filter(user=user)
    return render(req,'user/cart_display.html',{'data':data})  


def delete_cart(req,id):
    data=Cart.objects.get(pk=id) 
    data.delete()
    return redirect(cart_display)


def buy_pro(req,id):
    Product=product.objects.get(pk=id)
    user=User.objects.get(username=req.session['user'])
    price=Product.offer_price
    data=Buy.objects.create(user=user,product=Product,price=price)
    data.save()
    return redirect(user_home)


def user_view_bookings(req):
    user=User.objects.get(username=req.session['user'])
    data=Buy.objects.filter(user=user)[::-1]
    return render(req,'user/view_bookings.html',{'data':data})

