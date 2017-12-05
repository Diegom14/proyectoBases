from configuraciones import *
import psycopg2
conn = psycopg2.connect("dbname=%s user=%s password=%s"%(database,user,passwd))

cur = conn.cursor()


sql = """
CREATE TABLE personas
			(id serial PRIMARY KEY, rut INT,  dv int, cantidad_choques int, 
			edad int, nombre varchar(50), calle varchar(50), numeracion int, comuna varchar(50));	

CREATE TABLE vehiculo
			(id serial PRIMARY KEY, patente varchar(50),  personas_id int, 
			marca varchar(50), modelo varchar(50));	

CREATE TABLE conductor_choque
			(personas_id int, vehiculo_id int, choque_id int, alcoholemia numeric(11, 10), PRIMARY KEY(personas_id, vehiculo_id, choque_id));

CREATE TABLE choques
			(id serial PRIMARY KEY, vehiculo_id int, personas_id int, fecha timestamp, comuna varchar(50));
"""
cur.execute(sql)
conn.commit()
cur.close()
