from configuraciones import *
import psycopg2
conn = psycopg2.connect("dbname=%s user=%s password=%s"%(database,user,passwd))

cur = conn.cursor()


sql = """
CREATE TABLE personas
			(id serial PRIMARY KEY, rut INT,  dv varchar(1), cantidad_choques int, 
			edad int, nombre varchar(40), direccion varchar(40));	

CREATE TABLE vehiculo
			(id serial PRIMARY KEY, patente varchar(40),  personas_id int, 
			modelo varchar(40), marca varchar(20));	

CREATE TABLE conductor_choque
			(personas_id int, vehiculo_id int, choque_id int, alcoholemia numeric(11, 10), testimonio text);

CREATE TABLE choques
			(id serial PRIMARY KEY, vehiculo_id int, personas_id int, cantidad_fallecidos int, fecha varchar(10));
"""
cur.execute(sql)
conn.commit()
cur.close()
