from django.shortcuts import render, HttpResponse, redirect 
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login as auth_login
from . models import *
# Create your views here.
def index(request):
    return render(request,'home.html')


def invoice(request):
    if request.method == "POST":
        email=request.POST.get("inputEmail4")
        invoice_date=request.POST.get("inputdate")
        address=request.POST.get("inputAddress")
        address2=request.POST.get("inputAddress2")
        city=request.POST.get("inputCity")
        # State=request.POST.get("inputState")
        Invoice.objects.create(Email=email,Invoice_date=invoice_date,Address=address,Address2=address2,City=city,user=request.user)    
    return render(request,'invoice.html')

def register(request):
    if request.method=="POST":
        first_name=request.POST.get("fname",None)
        last_name=request.POST.get("lname",None)
        email=request.POST.get("email",None)
        password=request.POST.get("password",None)
        user = User.objects.create_user(username=email,email=email,first_name=first_name,last_name=last_name,password=password)
        return redirect("login")
    return render(request,'register.html')

def login(request):
    if request.method == "POST":
        Email=request.POST.get("email")
        password=request.POST.get("password")

        user=authenticate(username=Email,password=password)
        print(user)
        if not user:
            print("user not found, please register")
        else:
            print("user not found")
            auth_login(request,user)
            print(request.user)
        return redirect("invoice")
    return render(request,"login.html")

def viewsinvoice(request):
    invoices=Invoice.objects.all()
    context={"invoice1":invoices}
    print(invoices.first())

    return render(request,"viewsinvoice.html",context)

def deletinvoivce(request,pk):
    Invoice.objects.filter(id=pk).delete()
    invoices=Invoice.objects.all()
    context={"invoice1":invoices}

    return render(request,"viewsinvoice.html",context)   
    
    



        