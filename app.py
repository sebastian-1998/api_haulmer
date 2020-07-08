#importamos los archivos necesarios
from flask import Flask, jsonify, request
#ejecutamos flask
app = Flask(__name__)
#importamos las incidencias para poder mostrarlas
from incidencias import incidencias
#creamos la ruta para mostrar datos
@app.route('/incidencias')
def mostrar():
	return jsonify({"Lista de incidencias": incidencias})
#creamos la funcion para poder filtrar por titulo
@app.route('/incidencias/<string:titulo>')
def obtener_ncidencia(titulo):
	#con un ciclo for recorremos las incidencias y mientras recorre las incidencias va comparando si la id solicitada existe o no y si existe la retorna
	incidencia_encontrada = [incidencia for incidencia in incidencias if incidencia['titulo'] == titulo.lower()]
	#si ha encontrado un elemento entonces lo muestra
	if (len(incidencia_encontrada) > 0):
		return jsonify({'incidencia': incidencia_encontrada[0]})
	#si no ha encontrado nada que coincida muestra el mensaje
	return jsonify({'mensaje': 'incidencia no encontrada'})

@app.route('/incidencias', methods=['POST'])
#creamos la funcion para agregar productos
def agregar_incidencia():
	#creamos las variables necesarias y con request.json recibimos los datos relacionados con las variables desde el frontend
	nueva_incidencia = {
		"fecha": request.json['fecha'],
		"titulo": request.json['titulo'],
		"descripcion": request.json['descripcion'],
		"nombre_agente": request.json['nombre_agente'],
		"id": request.json['id']
	}
	#agregamos el dato
	incidencias.append(nueva_incidencia)
	#mostramos un json con la nueva lista de incidencias junto a un mensaje
	return jsonify({'mensaje': 'Incidencia agregada', 'incidencias': incidencias})

@app.route('/incidencias/<string:titulo>', methods=['PUT'])
#creamos la funcion para poder modificar una incidencia por su id
def modificar_incidencia(titulo):
	#con un ciclo for recorremos las incidencias y mientras recorre las incidencias va comparando si la id solicitada existe o no y si existe la retorna
	incidencia_encontrada = [incidencia for incidencia in incidencias if incidencia['titulo'] == titulo.lower()]
	#si ha encontrado un elemento entonces lo editamos
	if (len(incidencia_encontrada) > 0):
		incidencia_encontrada[0]['fecha'] = request.json['fecha']
		incidencia_encontrada[0]['descripcion'] = request.json['descripcion']
		#mostramos un mensaje
		return jsonify({"mensaje": "Incidencia actualizada",
			"incidencia": incidencia_encontrada[0]
			})
		#en caso de no encontrar nada muestra un mensaje
		return jsonify({"mensaje": "Incidencia no encontrada"})

@app.route('/incidencias/<string:titulo>', methods=['DELETE'])
#creamos el metodo para borrar incidencias
def borrar_incidencia(titulo):
	#con un ciclo for recorremos las incidencias y mientras recorre las incidencias va comparando si la id solicitada existe o no y si existe la retorna
	incidencia_encontrada = [incidencia for incidencia in incidencias if incidencia['titulo'] == titulo.lower()]
	#si ha encontrado un elemento entonces lo borramos
	if (len(incidencia_encontrada) > 0):
		#de la lista de incidencias borramos el elemento encontrado
		incidencias.remove(incidencia_encontrada[0])
		#devolvemos en un json la lista sin el elemento que se acaba de quitar
		return jsonify({"mensaje": "Incidencia eliminada",
			"Incidencias: ": incidencias
			})
	#en caso de no encontrar nada muestra un mensaje
	return jsonify({"mensaje": "Incidencia no encontrada"})
#iniciamos la app
if __name__ == '__main__':
	#usamos el modo debug para poder hacer cambios sin apagar el env
	app.run(debug=True, port=5000)