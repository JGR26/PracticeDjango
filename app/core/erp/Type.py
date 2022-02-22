from email.policy import default
from pickle import TRUE
from tabnanny import verbose
from django.db import models
from datetime import datetime

class Type(models.Model):
    name=models.CharField(max_length=150,verbose_name='Name',unique=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name= 'Tipo'
        verbose_name_plural= 'Tipos'
        db_table='Tipo'
        ordering=["id"]

