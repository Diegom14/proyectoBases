from app import app
from flask import render_template, request
from configuraciones import *
import psycopg2

conn = psycopg2.connect("dbname=%s user=%s password=%s"%(database,user,passwd))

cur = conn.cursor()


usuario ={} 
usuario["nombre"] = "Julio"
usuario["apellido"] = "Grande"
usuario["rol"]   = "Administrador"





@app.route('/')
def index():
	return render_template("digimon.html",usuario = usuario)


@app.route('/mostrar_personas', methods=["POST","GET"])
def mostrarPersona():
	if request.method == "POST":
		rut = request.form["rut"]
		sql = "select * from personas where rut = '%s'"%(rut)

		cur.execute(sql)
		conn.commit()
		resultados = cur.fetchall()
		return render_template("mostrarPersonas.html",usuario = usuario,resultados=resultados)
	else :
		return render_template("mostrarPersonas.html",usuario = usuario,resultados=[])


@app.route('/datos_personas', methods=["POST","GET"])
def formularioPersona():

	if request.method == "POST":
		



		nombre = request.form["nombre"]
		rut = request.form["rut"]
		
		dv = request.form["dv"]
		
		edad = request.form["edad"]
		direccion = request.form["direccion"]
		cantidadDeChoques = request.form["cantidad_choques"]
		 

		sql = "insert into personas(nombre, rut, dv, cantidad_choques, edad, direccion) values('%s','%s','%s','%s','%s','%s')"%(nombre, rut, dv, cantidadDeChoques, edad, direccion)

		cur.execute(sql)
		conn.commit()
		

	return render_template("formsPersonas.html",usuario = usuario)

@app.route('/datos_vehiculos', methods=["POST","GET"])
def formularioVehiculo():

	if request.method == "POST":
		patente = request.form["patente"]
		modelo = request.form["modelo"]
		
		marca = request.form["marca"]
		 

		sql = "insert into vehiculo(patente, modelo, marca) values('%s','%s','%s')"%(patente, modelo, marca)

		cur.execute(sql)
		conn.commit()
	return render_template("formsVehiculos.html",usuario = usuario)


@app.route('/datos_conductor', methods=["POST","GET"])
def formularioConductor():

	if request.method == "POST":
		
		alcoholemia = request.form["alcoholemia"]
		testimonio = request.form["testimonio"]
		 

		sql = "insert into conductor_choques(alcoholemia) values('%s','%s')"%(alcoholemia, testimonio)

		cur.execute(sql)
		conn.commit()
	return render_template("formsConductor.html",usuario = usuario)


@app.route('/datos_choques', methods=["POST","GET"])
def formularioChoques():

	if request.method == "POST":
		cantidadFallecidos = request.form["cantidad_fallecidos"]
		fecha = request.form["fecha"]
		
		
		 

		sql = "insert into choques(cantidad_fallecidos, fecha) values('%s','%s')"%(cantidadFallecidos, fecha)

		cur.execute(sql)
		conn.commit()
	return render_template("formsChoques.html",usuario = usuario)




	








