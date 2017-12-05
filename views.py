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
	return render_template("index.html",usuario = usuario)




@app.route('/mostrar_personas', methods=["POST","GET"])
def mostrarPersona():
	if request.method == "POST":
		rut = request.form["rut"]
		dv = request.form["dv"]
		sql = "select * from personas where rut = %s and dv = %s"%(rut, dv)

		cur.execute(sql)

		conn.commit()
		resultados = cur.fetchall()
		if len(resultados) > 0:

			return render_template("mostrarPersonas.html",usuario = usuario,resultados=resultados)
		else:
			return render_template("mostrarPersonas.html",usuario = usuario, advertencia = "Rut no registrado")
	
	
	return render_template("mostrarPersonas.html",usuario = usuario)


#INSERT 

#listo
@app.route('/datos_personas', methods=["POST","GET"])
def formularioPersona():

	if request.method == "POST":
		



		nombre = request.form["nombre"]
		rut = request.form["rut"]
		
		dv = request.form["dv"]
		
		edad = request.form["edad"]
		calle = request.form["calle"]
		numeracion = request.form["numeracion"]
		cantidadDeChoques = 1
		comuna = request.form["comuna"]	

		cur.execute("select personas.id from personas where rut = %s and dv =%s"%(rut,dv))	 

		test = cur.fetchall()

		if len(test) == 0:
			sql = "insert into personas(nombre, rut, dv, cantidad_choques, edad, calle, numeracion, comuna) values('%s', %s, %s, '%s', %s,'%s', %s, '%s')"%(nombre, rut, dv, cantidadDeChoques, edad, calle, numeracion, comuna)

			cur.execute(sql)
			conn.commit()
			return render_template("formsPersonas.html",usuario = usuario, advertencia = "Persona agregada")
		else:
			return render_template("formsPersonas.html",usuario = usuario, advertencia = "El rut ingresado ya se encuentra registrado")
		

	return render_template("formsPersonas.html",usuario = usuario)

@app.route('/datos_vehiculos', methods=["POST","GET"])
def formularioVehiculo():

	if request.method == "POST":
		patente = request.form["patente"]
		modelo = request.form["modelo"]
		
		marca = request.form["marca"]
		rut = request.form["rut"]
		dv = request.form["dv"]
		sql = "select id from personas where rut = %s and dv = %s"%(rut, dv)

		cur.execute(sql)
		idPersona = cur.fetchall()

		
		

		cur.execute("select vehiculo.id from vehiculo where patente = '%s'"%(patente))
		test = cur.fetchall()

		if len(idPersona) == 0:
			return render_template("formsVehiculos.html",usuario = usuario, advertencia = "Rut no registrado")

		elif len(test) == 0:
			idProp = idPersona[0][0]
			cur.execute("insert into vehiculo(patente, modelo, marca, personas_id) values('%s','%s','%s',%s);"%(patente, modelo, marca,idProp))
			conn.commit()
			return render_template("formsVehiculos.html",usuario = usuario, advertencia = "Vehiculo agregado con exito")
			
		else:
			
			return render_template("formsVehiculos.html",usuario = usuario, advertencia = "Patente ya esta registrada")
		
		
	return render_template("formsVehiculos.html",usuario = usuario)

@app.route('/Informacion_choques', methods=["POST","GET"])
def informacionChoque():

	if request.method == "POST":
		
		alcoholemia = request.form["alcoholemia"]

		
		rut = request.form["rut"]
		
		dv = request.form["dv"]
		patente = request.form["patente"]

		cur.execute("select vehiculo.id from vehiculo where patente ='%s'"%(patente))
		vehicId = cur.fetchall()
		
		
		
		comuna_choque = request.form["comuna_choque"]	 
		cur.execute("select personas.id from personas where rut = %s and dv = %s"%(rut, dv))
		prueba = cur.fetchall()
		if len(prueba) == 0:
			
			return render_template("informacionChoque.html",usuario = usuario, advertencia = "Persona no registrada")
		
		elif len(vehiId) == 0:

			return render_template("informacionChoque.html",usuario = usuario, advertencia = "Vehiculo no registrado")


		else:

			vehiculoId = vehicId[0][0]
			cur.execute("update personas set cantidad_choques = cantidad_choques + 1 where rut = %s and dv = %s"%(rut, dv))
			
			cur.execute("select id from personas where rut = %s and dv = %s;"%(rut, dv))
			idPro = cur.fetchall()
			idProp = idPro[0][0]

			cur.execute("insert into choques(personas_id, vehiculo_id, comuna) values(%s, %s,'%s')"%(idProp, vehiculoId, comuna_choque))
			

			conn.commit()

			cur.execute("select choques.id from choques where personas_id =%s and vehiculo_id = %s"%(idProp,vehiculoId))
			choquesId = cur.fetchall()
			choqueId = choquesId[0][0]

			sql2 = "insert into conductor_choque(personas_id, vehiculo_id, choque_id, alcoholemia) values(%s, %s, %s, %s)"%(idProp, vehiculoId, choqueId, alcoholemia)

			cur.execute(sql2)

			return render_template("informacionChoque.html",usuario = usuario, advertencia = "Datos agregados")
		
		 

		
		
				

		

		
	return render_template("informacionChoque.html",usuario = usuario)


#DELETE
@app.route('/eliminar_vehiculo', methods=["POST","GET"])
def eliminarVehiculo():
	if request.method == "POST":

		patente = request.form["patente"]
		propietario = request.form["propietario"]
		dv = request.form["dv"]
		cur.execute("select vehiculo.id from vehiculo where patente = '%s'"%(patente))
		test = cur.fetchall()
		cur.execute("select personas.id from personas where rut =%s and dv =%s"%(propietario,dv))
		test2 = cur.fetchall()
		if len(test) == 0:
			return render_template("eliminarVehiculo.html",usuario = usuario, advertencia = "Patente no se encuentra registrada")
		elif len(test2) ==0:
			return render_template("eliminarVehiculo.html",usuario = usuario, advertencia = "Rut no se encuentra registrado")

		else:
			sql = "delete from vehiculo where vehiculo.personas_id in (select personas.id from personas where personas.rut = %s and personas.dv = %s) and vehiculo.patente = '%s'"%(propietario, dv, patente)
			cur.execute(sql)
			conn.commit()
			return render_template("eliminarVehiculo.html",usuario = usuario, advertencia = "Vehiculo eliminado")

		
	return render_template("eliminarVehiculo.html",usuario = usuario)


@app.route('/eliminar_persona', methods=["POST","GET"])
def eliminarPersona():
	if request.method == "POST":

		rut = request.form["rut"]
		dv = request.form["dv"]
		cur.execute("select vehiculo.id from personas, vehiculo where personas.id = vehiculo.personas_id and rut = %s and dv = %s;"%(rut, dv))

		test = cur.fetchall()
		cur.execute("select personas.id from personas where rut = %s and dv = %s"%(rut, dv))
		test2 = cur.fetchall()



		if len(test2) == 0:
			return render_template("eliminarPersona.html",usuario = usuario, advertencia = "Rut no se encuentra registrado en la base de datos")
		

		if len(test) ==0:
			sql = "delete from personas where personas.rut = %s and dv = %s;"%(rut, dv)
			cur.execute(sql)
			conn.commit()
			return render_template("eliminarPersona.html",usuario = usuario, advertencia = "Persona eliminada")
		
		else:
			return render_template("eliminarPersona.html",usuario = usuario, advertencia = "No se puede eliminar, la persona tiene un vehiculo")
		
	return render_template("eliminarPersona.html",usuario = usuario)
	

#UPDATE
@app.route('/actualizar_direccion', methods=["POST","GET"])
def actualizarDireccion():
	if request.method == "POST":

		calle = request.form["calle"]
		numeracion = request.form["numeracion"]
		rut = request.form["rut"]
		dv = request.form["dv"]
		comuna = request.form["comuna"]

		cur.execute("select personas.id from personas where rut = %s and dv = '%s'"%(rut, dv))
		test = cur.fetchall()

		if len(test) > 0:


			sql = "update personas set calle = '%s', numeracion = %s where rut = %s and dv = %s"%(calle, numeracion, rut, dv)

			cur.execute(sql)
			conn.commit()
		else:
			return render_template("actualizarDireccion.html",usuario = usuario, advertencia = "Rut no registrado")			
	return render_template("actualizarDireccion.html",usuario = usuario)


@app.route('/mostrar_alcoholemia', methods=["POST","GET"])
def verificarAlcoholemia():
	if request.method == "POST":

		
		
		sql = "select personas.rut from personas, conductor_choque where alcoholemia > 0.8 and personas.id = conductor_choque.personas_id group by personas.id;"

		cur.execute(sql)
		conn.commit()
		ebrios = cur.fetchall()

		
		return render_template("ebriedad.html",usuario = usuario, ebrios = ebrios)
	else :
		return render_template("ebriedad.html",usuario = usuario,ebrios=[])

@app.route('/choques_comuna', methods=["POST","GET"])
def choquesComuna():
	if request.method == "POST":

		comuna = request.form["comuna"]
		
		cur.execute("select count(*) from choques where comuna ='%s'"%(comuna))
		cantidad = cur.fetchall()

		if len(cantidad) == 0:
			return render_template("choquesComuna.html",usuario = usuario, cantidad = [])
		else:
			
			conn.commit()
			return render_template("choquesComuna.html",usuario = usuario, cantidad = cantidad)
		

		
		
	else :
		return render_template("choquesComuna.html",usuario = usuario,cantidad=[])


@app.route('/choques_marca', methods=["POST","GET"])
def choquesMarca():
	if request.method == "POST":

		marca = request.form["marca"]
		modelo = request.form["modelo"]

		cur.execute("select vehiculo.id from vehiculo where marca = '%s' and modelo = '%s';"%(marca,modelo))
		test = cur.fetchall()

		if len(test) > 0:
			cur.execute("select count(*) from choques, vehiculo where choques.vehiculo_id = vehiculo.id and marca = '%s' and modelo = '%s';"%(marca,modelo))
			conn.commit()
			cantidad = cur.fetchall()

			return render_template("choquesMarca.html",usuario = usuario,cantidad=cantidad)
		
		else:
			return render_template("choquesMarca.html",usuario = usuario,cantidad=[], advertencia = "No registrado")
	else :
		return render_template("choquesMarca.html",usuario = usuario,cantidad=[])






#sql = "select personas.rut from personas, conductor_choque where alcoholemia > 0.3 and alcoholemia <0.8 and personas.id = conductor_choque.personas_id;"
#		cur.execute(sql)
#		conn.commit()
#		influencia = cur.fetchall()














	








