from email.policy import default
from pickle import TRUE
from tabnanny import verbose
from django.db import models
from datetime import datetime

class Category(models.Model):
    name=models.CharField(max_length=150,verbose_name='Name')

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name= 'Categoria'
        verbose_name_plural= 'Categorias'
        db_table='Categoria'
        ordering=["id"]