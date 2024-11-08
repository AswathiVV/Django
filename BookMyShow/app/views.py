from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from .models import *
# Create your views here.
def bms(req):
    data=movie.objects.all()
    return render(req,'bms.html',{'data':data})

def view_movie(req,id):
    data=movie.objects.get(pk=id)
    Member=Members.objects.filter(movie=data)
    return render (req,'bms_p1.html',{'data':data,'member':Member})