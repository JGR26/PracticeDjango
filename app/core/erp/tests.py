

from msilib import type_key
from config.wsgi import *
from core.erp.Type import Type
#Listar
query=Type.objects.all()
print(query)

#Insert
""" try:
    t=Type()
    t.name="Tes2"
    t.save()
except Exception as e:
    print(e) """



#Edicion

""" t=Type.objects.get(pk=1)
t.name="jdjds"
t.save() """

""" t=Type.objects.get(pk=1)
t.delete() """

obj=Type.objects.filter()
print(obj)
