from django.shortcuts import render,redirect
from .forms import *
from . models import *

# Create your views here.
def index(request):
    if request.method=="POST":
        data=Vehicle.objects.filter()
        form=VehicleForm(request.POST,request.FILES)
        if form.is_valid():
            f=form.save()
            f.save()
            
            return render(request,'view.html',{'data':data,'message':'Vehicle Add Successfully'})
        else:
            form=VehicleForm()
            return render(request,'index.html',{'form':form})
    else:

        
        form = VehicleForm()


        return render(request,'index.html',{'form':form})


def view(request):
    data=Vehicle.objects.filter()
    return render(request,'view.html',{'data':data})

def update(request,pk):
    
    if request.method=='POST':
        data=Vehicle.objects.get(pk=pk)

        form=VehicleForm(request.POST or None ,instance=data)
        if form.is_valid():
            form.save()
            return render(request,'base.html',{'message':'Vehicle update Successfully'})
            
    else:
        data=Vehicle.objects.get(pk=pk)
        form=VehicleForm(instance=data)
        return render(request,'update.html',{'form':form,'data': data})


def delete(request,pk):
    data=Vehicle.objects.get(pk=pk)
    data.delete()
    data=Vehicle.objects.all()
    return render(request,'view.html',{'data':data,'message':'Vehicle Delete Successfully'})
    