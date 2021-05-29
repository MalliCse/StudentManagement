from django.db import models


class Insert(models.Model):
    empname = models.CharField(max_length=10)
    email= models.CharField(max_length=10)
    password=models.CharField(max_length=10)

class Register(models.Model):
    stdname = models.CharField(max_length=20,unique=True)
    email= models.CharField(max_length=20,null=True,unique=True)
    stdid=models.CharField(max_length=10,unique=True)
    password=models.CharField(max_length=10,unique=True)
    gender=models.CharField(max_length=6)
    total_fee=models.CharField(max_length=5,null=True)
    paid_fee=models.CharField(max_length=5,null=True)
    dob=models.CharField(max_length=11,null=True)
    contact=models.CharField(max_length=10,unique=True)
    address=models.TextField(max_length=50,null=True)

    

 