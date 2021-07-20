from django.shortcuts import render,redirect
from django.http import HttpResponseBadRequest, request
from django.contrib.auth.models import User,auth
from portfolio.models import contact
from django.contrib import messages

# Create your views here.
def portfolio(request):
    
     return render(request,'index.html')


def Contact(request):
    if request.method=='POST':
        name=request.POST['name']
        email=request.POST['email']
        phone=request.POST['phone']
        message=request.POST['message']
        print(name,email,phone,message)
        Contact=contact(name=name,email=email ,phone=phone,message=message)
        Contact.save()
        
        messages.success(request,'Message sent successfully') 
        return redirect('Contact')
        
       
    return render(request,'index.html',{messages:'messages'})
       