from django.db import models

# Create your models here.

class Profile(models.Model):
    name = models.CharField(max_length=40)
    phone = models.CharField(max_length=12)
    email = models.CharField(max_length=25)
    whatsappno = models.CharField(max_length=12)
    adhaarno = models.CharField(max_length=15)
    city = models.CharField(max_length=25)
    state = models.CharField(max_length=25)
    pincode = models.CharField(max_length=20)
    pan = models.CharField(max_length=20)
    bankacctno = models.CharField(max_length=40)
    bankName = models.CharField(max_length=50)
    bankIFSC = models.CharField(max_length=15)
    loanamt = models.DecimalField(max_digits=20,decimal_places=2)
    loantype = models.CharField(max_length=15)
    itr = models.CharField(max_length=20)
    tenure = models.CharField(max_length=10)
    date = models.DateField(auto_now_add=True)
    status = models.CharField(max_length=25)



class Payment(models.Model):
    profile = models.ForeignKey(Profile,on_delete=models.CASCADE)
    amount = models.CharField(max_length=30)
    date = models.DateField(auto_now_add=True)
