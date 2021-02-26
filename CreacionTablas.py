'''
Created on 23 ene. 2021

@author: Ivan
'''

import psycopg2
import psycopg2.extras
import sys
import pprint
import sqlite3
#postgres root
#openpg openpgpwd
conx = psycopg2.connect("dbname=Polideportivo user=postgres password=root")
cur = conx.cursor()

def creacionTablas():
    crearClientes()
    crearDeportes()
    crearMatriculas()
    cur.close()
    conx.commit()
    conx.close()

def crearClientes():
    try:
        cur.execute("""CREATE TABLE clientes (
                dni VARCHAR(10) PRIMARY KEY,
                nombre VARCHAR(100) NOT NULL,
                fnac VARCHAR(10) NOT NULL,
                telefono INTEGER)""")
    except:
        print("La tabla de Clientes ya existe.")
    else:
        print("La tabla de Clientes se ha creado correctamente.")
    
def crearDeportes():
    try:
        cur.execute("""CREATE TABLE deportes (
                nombre VARCHAR(100) PRIMARY KEY,
                precio INTEGER NOT NULL)""")
    except:
        print("La tabla de Deportes ya existe.")
    else:
        print("La tabla de Deportes se ha creado correctamente.")
    
def crearMatriculas():
    try:
        cur.execute('''CREATE TABLE matriculas (
                horario VARCHAR(50) NOT NULL,
                nombre VARCHAR(100),
                dni VARCHAR(10),
                FOREIGN KEY (nombre)
                REFERENCES deportes (nombre),
                FOREIGN KEY (dni)
                REFERENCES clientes (dni))''')
    except:
        print("La tabla de Matriculas ya existe.")
    else:
        print("La tabla de Matriculas se ha creado correctamente.")