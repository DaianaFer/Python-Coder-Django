from datetime import datetime
from django.http import HttpResponse

def hello(request):
    return HttpResponse ("Hola coders")

def hora_actual(request):
    hora_a = datetime.now()    
    
    return HttpResponse (f"<h1>{hora_a}</h1>")

def calcular_nacimiento(request, edad):
    
     año_actual= 2022
     año_nacimiento= año_actual - int(edad)    

     return HttpResponse (f"Usted nacio en el año {año_nacimiento}")