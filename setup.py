from configuraciones import *
import psycopg2
conn = psycopg2.connect("dbname=%s user=%s password=%s"%(database,user,passwd))

cur = conn.cursor()
sql = """DROP SCHEMA public CASCADE;
CREATE SHEMA public;"""

cur.execute(sql)

sql = """
CREATE TABLE personas
			(id serial PRIMARY KEY, rut int(8),  dv varchar(1), cantidad_choques int(10), edad int(10), nombre varchar(10), apellido varchar(10), direccion varchar(40));	

CREATE TABLE vehiculo
			(id serial PRIMARY KEY, patente varchar(40),  personas_id int(100), modelo varchar(40), marca varchar(20), dueño_id int(10));	

CREATE TABLE conductor_choque
			(personas_id int(10), vehiculo_id int(10), choque_id int(10), testimonio text, alcoholemia int(10));

CREATE TABLE choques
			(id serial PRIMARY KEY, vehiculo_id int(10), personas_id int(10), fallecidos int(100), fecha varchar(10));
"""
cur.execute(sql)
