from django.shortcuts import render,redirect
from django.http import request,HttpResponse
from work.models import Work
from work.forms import *

def index(request):
    if request.method=="POST":
        form=WorkForm(request.POST, request.FILES)

        if(form.is_valid()):
            form.save()
            return redirect('/fronts')
    else:
        form=WorkForm()
    return render(request,'index.html',{'form':form})

def fronts(request):
    return render(request,'display.html',{
            'display':Work.objects.all(), })

