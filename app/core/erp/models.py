from email.policy import default
from pickle import TRUE
from django.db import models
from datetime import datetime
from core.erp.Category import Category
import core.erp.Type as Type

class Employee(models.Model):
    categ=models.ManyToManyField(Category)
    type=models.ForeignKey(Type.Type, on_delete=models.CASCADE)
    names=models.CharField(max_length=150,verbose_name='Names')
    dni=models.CharField(max_length=10,unique=True,verbose_name='DNI')
    date_joined=models.DateField(default=datetime.now,verbose_name='Fecha de registro')
    date_created=models.DateTimeField(auto_now=True)
    date_updated=models.DateTimeField(auto_now_add=True)
    age= models.PositiveIntegerField(default=0)
    salary=models.DecimalField(default=0.00,max_digits=9,decimal_places=2)
    state=models.BooleanField(default=True)
    gender=models.CharField(max_length=50)
    avatar=models.ImageField(upload_to='avatar/%Y/%m/%d',null=True,blank=True)
    curriculum=models.FileField(upload_to='cv/%Y/%m/%d',null=True,blank=True)

    def __str__(self):
        return self.names

    class Meta:
        verbose_name= 'Empleado'
        verbose_name_plural= 'Empleados'
        db_table='Empleado'
        ordering=["id"]


