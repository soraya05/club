from django.shortcuts import render
from socios.models import Cuota 

# Create your views here.
def cuota_al_dia (request, numero_socio):
	cuota = Cuota.objects.filter(socio__numero=numero_socio).last()
	return render(request, 'cuota.html', {'ultima_cuota': cuota})
