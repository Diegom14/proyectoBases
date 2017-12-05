from configuraciones import *
import psycopg2
conn = psycopg2.connect("dbname=%s user=%s password=%s"%(database,user,passwd))
cur = conn.cursor()

sql =""" 
INSERT INTO personas (rut, dv, cantidad_choques, edad, nombre, calle, numeracion, comuna) values (11111111, 1, 1, 27, 'JUAN SOTO', 'ejercito', 4, 'comuna1');
 
INSERT INTO personas (rut, dv, cantidad_choques, edad, nombre, calle, numeracion, comuna) values (22222222, 2, 1, 23, 'ROBERTO DIAZ', 'ejercito', 5, 'comuna2');

INSERT INTO personas (rut, dv, cantidad_choques, edad, nombre, calle, numeracion, comuna) values (12345678, 3, 1, 39, 'JUANA DE ARCO', 'ejercito', 2, 'comuna3');
 
INSERT INTO personas (rut, dv, cantidad_choques, edad, nombre, calle, numeracion, comuna) values (12345434, 4, 1, 32, 'MARIA MONTT', 'ejercito', 1, 'comuna4');

INSERT INTO vehiculo (patente, personas_id, modelo, marca) values ('hdf21', 2, 'modelo1', 'marca4' );

INSERT INTO vehiculo (patente, personas_id, modelo, marca) values ('KJf21', 1, 'modelo2', 'marca1' );

INSERT INTO vehiculo (patente, personas_id, modelo, marca) values ('hlo31', 3, 'modelo3', 'marca2' );

INSERT INTO choques (vehiculo_id, personas_id,  comuna) values (1, 1, 'comuna1');

INSERT INTO choques (vehiculo_id, personas_id, comuna) values (2, 2, 'comuna2');

INSERT INTO choques (vehiculo_id, personas_id, comuna) values (3, 3, 'comuna3');

INSERT INTO choques (vehiculo_id, personas_id, comuna) values (2, 4, 'comuna4');

INSERT INTO choques (vehiculo_id, personas_id, comuna) values (1, 1, 'comuna4');

INSERT INTO choques (vehiculo_id, personas_id, comuna) values (2, 1, 'comuna1');

INSERT INTO choques (vehiculo_id, personas_id, comuna) values (2, 1, 'comuna1');

INSERT INTO conductor_choque (personas_id, vehiculo_id, choque_id, alcoholemia) values (1, 2, 1, 1.1);


 """
cur.execute(sql)
conn.commit()
cur.close()
