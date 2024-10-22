from django.shortcuts import render,redirect
from django.http import HttpResponse
# Create your views here.


def fun1(request):
    return HttpResponse("fun1")

def fun2(request):
    a={'name':'manu','age':34}
    return HttpResponse(a)

def fun3(req,a,b):
    return HttpResponse(a)

def fun4(req,a,b,c):           # enter 3 numbers and findout which one is largest
    if a>b and a>c:
        return HttpResponse(a)
    elif b>a and b>c:
        return HttpResponse(b)
    else:
        return HttpResponse(c)
    # print(type(a))
    # return HttpResponse(a)
def index_page(req):
    name="Akhil"
    age="20"
    place="Knr"
    return render(req,'index.html',{"name":name,"age":age,"place":place})   
 
def demo(req):
    l=[{'name':'anu','age':20,'place':'knr'},{'name':'tyra','age':21,'place':'knr'},{'name':'sam','age':23,'place':'knr'}]
    d={'name':'anu','age':20}
    return render(req,"demo.html",{"data":l,'data1':d})

def snd(req):
    return render(req,"second.html")

todo=[{'id':'1','task':'task1'},{'id':'2','task':'task2'}]
def fun(request):
    if request.method=='POST':
        id=request.POST['id']
        task=request.POST['task']
        todo.append({'id':id,'task':task})
        print(todo)
        return redirect(fun)
    return render(request,'todo.html',{'todo':todo})


def form2(request,id):
    task=' '
    for i in todo:
        if i['id']==id:
            task=i
    if request.method=='POST':
        id=request.POST['id']
        task1=request.POST['task']
        task['id']=id
        task['task']=task1
        
        return redirect(fun)
    return render(request,'form.html',{'data':task})


def delete(request,id):
    for i in todo:
        if i['id']==id:
            todo.remove(i)
    return redirect(fun)               






    