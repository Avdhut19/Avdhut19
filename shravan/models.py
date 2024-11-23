from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Invoice(models.Model):
    Email=models.CharField(max_length=25,null=True,blank=True)
    Invoice_date=models.DateField(null=True,blank=True)
    Address=models.CharField(max_length=25,blank=True)
    Address2=models.CharField(max_length=25,blank=True)
    City=models.CharField(max_length=25,blank=True)
    # State=models.CharField(max_length=25,blank=True)

    user=models.ForeignKey(User,related_name="invoice",on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.Email