from django.shortcuts import render
from PriApp.models import Familia

# Create your views here.

def mostrar_flia(request):
    f1 = Familia(nombre='Adrian', apellido='Gonzalez', parentesco='esposo', edad=50, fec_nac='1972-10-20')
    f2 = Familia(nombre='Melisa', apellido='Gonzalez', parentesco='hija', edad=26, fec_nac='1996-02-08')
    f3 = Familia(nombre='Chiara', apellido='Gonzalez', parentesco='hija', edad=23, fec_nac='1999-01-15')
    f4 = Familia(nombre='Bianca', apellido='Gonzalez', parentesco='hija', edad=21, fec_nac='2000-09-11')
    return render(request, 'PriApp/Templates/Familia.html', {'Familia':[f1,f2,f3,f4]})


