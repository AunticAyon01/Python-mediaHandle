from django.shortcuts import render
from phones.models import Phone

def home(request):
    phn = Phone.objects.all()
    return render(request,'home.html',{'phn':phn})