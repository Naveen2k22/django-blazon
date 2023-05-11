from datetime import timedelta

from django.db import models
from django.utils import timezone

class Vendor(models.Model):
    class VendorsType(models.TextChoices):
        MANUFACTURER = "Manufacturer"
        WHOLESALER = "Wholesaler"
        RETAILER = "Retailer"
        SERVICE_PROVIDER = "Service/Maintenance Provider"
        INDEPENDENT = "Independent"
    
    name = models.CharField(max_length=200, blank=False, unique=True)
    vendor_type = models.CharField(max_length=28,choices=VendorsType.choices,blank=False)
    email = models.EmailField(max_length=254, blank=False)
    phone = models.CharField(max_length=13)
    about = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_created=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self) -> str:
        return self.name
    
    def is_created_recently(self):
        return self.created_at >= timezone.now() - timedelta(days=-1)


class User(models.Model):
    class GenderType(models.TextChoices):
        MALE = 'm', 'Male'
        FEMALE = 'f', 'Female'
        TRANSGENDER = 'tr', 'Transgender'
    
    f_name = models.CharField(max_length=28)
    m_name = models.CharField(max_length=28, blank=True)
    l_name = models.CharField(max_length=28)
    gender = models.CharField(max_length=11, choices=GenderType.choices,default='m' )
    address = models.CharField(max_length=128, blank=False)
    email = models.EmailField(max_length=254, unique=True)
    phone = models.CharField(max_length=13, blank=True)
    
    def __str__(self) -> str:
        return self.f_name + self.m_name + self.l_name

class Desig(models.Model):
    title = models.CharField(max_length=128, unique=True)
    description = models.CharField(max_length=256, blank=True)
    
    def __str__(self) -> str:
        return self.title

class DesigGrade(models.Model):
    grade = models.CharField(max_length=128, unique=True)
    from_amt = models.DecimalField(max_digits=8, decimal_places=2)
    to_amt = models.DecimalField(max_digits=8, decimal_places=2)
    desig = models.ForeignKey(Desig, on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return self.grade