from configuraciones import *
import psycopg2
conn = psycopg2.connect("dbname=%s user=%s password=%s"%(database,user,passwd))
cur = conn.cursor()

sql ="""
INSERT INTO personas (rut, dv, cantidad_choques, edad) values (165455, "?", 1, 27)
 """
sql ="""
INSERT INTO personas (rut, dv, cantidad_choques, edad) values (195421, "?", 1, 23)
 """
sql ="""
INSERT INTO personas (rut, dv, cantidad_choques, edad) values (128554, "?", 1, 39)
 """
sql ="""
INSERT INTO personas (rut, dv, cantidad_choques, edad) values (130544, "?", 1, 32)
 """
sql ="""
"""
