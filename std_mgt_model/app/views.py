from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import*
# Create your views here.
def fun1(req):
    return HttpResponse ("Welcome")

def disp_std(req):
    data=Student.objects.all()
    return render(req,'display_std.html',{'data':data})

todo=[{'id':'1','task':'task1'},{'id':'2','task':'task2'}]
def fun(request):
    if request.method=='POST':
        roll_no=request.POST['roll_no']
        name=request.POST['name']
        age=request.POST['age']
        email=request.POST['email']
        phno=request.POST['phno']
        
        todo.append({'roll_no':roll_no,'name':name,'age':age,'email':email,'phno':phno})
        print(todo)
        return redirect(fun)
    return render(request,'std_add.html',{'todo':todo})


def form2(request,id):
    roll_no=' '
    for i in todo:
        if i['id']==id:
            task=i
    if request.method=='POST':
        roll_no=request.POST['roll_no']
        name=request.POST['name']
        age=request.POST['age']
        email=request.POST['email']
        phno=request.POST['phno']
        
        task['roll_no']=roll_no
        task['name']=name
        task['age']=age
        task['email']=email
        task['phno']=phno
        
        return redirect(fun)
    return render(request,'std_add.html',{'data':task})
