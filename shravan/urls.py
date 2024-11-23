
from django.urls import path
from.views import*
from . import views

urlpatterns =[
    path("",index,name="home"),
    path("login/",login,name="login"),
    path("register/",register,name="register"),
    path("invoice/",invoice,name="invoice"),
    path("viewsinvoice/",views.viewsinvoice,name="viewsinvoice"),
    path("deletinvoivce/<int:pk>",views.deletinvoivce,name="deletinvoivce")
    ]