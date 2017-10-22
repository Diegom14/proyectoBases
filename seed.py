from configuraciones import *
import psycopg2
conn = psycopg2.connect("dbname=%s user=%s password=%s"%(database,user,passwd))
cur = conn.cursor()

sql =""" 
INSERT INTO personas (rut, dv, cantidad_choques, edad, nombre, direccion) values (165455, '1', 1, 27, 'JUAN SOTO', 'ejercito 4');
 
INSERT INTO personas (rut, dv, cantidad_choques, edad, nombre, direccion) values (195421, '2', 1, 23, 'ROBERTO DIAZ', 'ejercito 5');

INSERT INTO personas (rut, dv, cantidad_choques, edad, nombre, direccion) values (128554, '3', 1, 39, 'JUANA DE ARCO', 'ejercito 2');
 
INSERT INTO personas (rut, dv, cantidad_choques, edad, nombre, direccion) values (130544, '4', 1, 32, 'MARIA MONTT', 'ejercito 1');

INSERT INTO vehiculo (patente, personas_id, modelo, marca) values ('hdf21', 2, '48 GTB', 'FERRARI' );

INSERT INTO vehiculo (patente, personas_id, modelo, marca) values ('KJf21', 1, 'MORNING', 'KYA' );

INSERT INTO vehiculo (patente, personas_id, modelo, marca) values ('hlo31', 3, 'SWIFT', 'SUZUKI' );

INSERT INTO choques (vehiculo_id, personas_id, cantidad_fallecidos, fecha) values (2, 1, 0, '11-5-2011');

INSERT INTO conductor_choque (personas_id, vehiculo_id, choque_id, testimonio, alcoholemia) values (1, 2, 1, 'conductor ebrio', 1.1);


 """
cur.execute(sql)
conn.commit()
cur.close()
