from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

from .models import Tjuegos

def pagina_de_prueba(request):
	return HttpResponse("<h1>Hola Caracols</h1>");

def devolver_juegos(request):
	lista=Tjuegos.objects.all()
	respuesta_final = []
	for fila_sql in lista:
		diccionario ={}
		diccionario['id'] = fila_sql.id
		diccionario['nombre'] = fila_sql.nombre
		diccionario['precio'] = fila_sql.precio
		respuesta_final.append(diccionario)
	return JsonResponse(respuesta_final,safe=False)

# Create your views here.

def devolver_juegos_por_id(request, id_solicitado):
	juegos = Tjuegos.objects.get (id = id_solicitado)
	comentarios = juegos.tcomentarios_set.all()
	lista_comentarios = []
	for fila_comentario_sql in comentarios:
		diccionario = {}
		diccionario['id'] = fila_comentario_sql.id
		
	resultado = {
		'id': juegos.id,
		'nombre': juegos.nombre,
		'precio': juegos.precio,
		
	}
	return JsonResponse(resultado, json_dumps_params={'ensure_ascii': False})

