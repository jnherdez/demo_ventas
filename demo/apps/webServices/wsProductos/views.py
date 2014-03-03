# Create your views here.
from django.http import HttpResponse
from demo.apps.ventas.models import producto
#Integramos la serializacion de los objetos
from django.core import serializers

def wsProductos_view(request):
	data = serializers.serialize("json", producto.objects.filter(status=True))
	#retorna la info en formato JSON
	return HttpResponse(data, mimetype='application/json')	