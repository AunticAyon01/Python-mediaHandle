from django.db.models import Model
from django.shortcuts import render, redirect

from .forms import PhoneForm
from .models import Phone


# Create your views here.
def create_phone(request):
    if request.method =='POST':
        form = PhoneForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = PhoneForm()
        return render(request,'forms.html',{'form':form})

def update_phone(request,id):
    p = Phone.objects.get(id=id)
    if request.method =='POST':
        form = PhoneForm(request.POST,request.FILES,instance=p)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = PhoneForm(instance=p)
        return render(request,'forms.html',{'form':form})

def delete_phone(request,id):
    Phone.objects.get(id=id).delete()
    return redirect('/')

