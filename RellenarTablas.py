'''
Created on 5 feb. 2021

@author: Ivan
'''
import psycopg2
import psycopg2.extras
import sys
import pprint
import sqlite3
import Cliente
import Deporte

#postgres root
#user=postgres password=root
def rellenarDeportes():
    conx = psycopg2.connect("dbname=Polideportivo user=postgres password=root")
    cur = conx.cursor()
    deportes = ["tenis", "natacion", "atletismo", "baloncesto", "futbol"]
    precios = [10,20,30,20,40]
    i=0
    try:
        for x in deportes:
            query = """INSERT INTO deportes(nombre, precio) VALUES(%s,%s)"""
            cur.execute(query,(x,precios[i]))
            i+=1
        print("Se ha rellenado la tabla deportes")
    except:
        print("Ya existen los datos")
    cur.close()
    conx.commit()
    conx.close()

def altaCliente(Cliente):
    conx = psycopg2.connect("dbname=Polideportivo user=postgres password=root")
    cur = conx.cursor()
    query = """INSERT INTO clientes(nombre, dni, fnac, telefono) VALUES(%s,%s,%s,%s)"""
    cur.execute(query,(Cliente.nombre,Cliente.dni,Cliente.fnac, Cliente.telefono))
    print("Se ha dado de alta correctamente")
    cur.close()
    conx.commit()
    conx.close()
    
def bajatCliente(dni):
    conx = psycopg2.connect("dbname=Polideportivo user=postgres password=root")
    cur = conx.cursor()
    query = """Delete from clientes where dni=%s"""
    try:    
        cur.execute(query,(dni,))
        print("Se ha dado de baja correctamente")
    except:
        print("No existe ningun cliente con ese dni")
    cur.close()
    conx.commit()
    conx.close()
    
def buscarCliente(dni):
    conx = psycopg2.connect("dbname=Polideportivo user=postgres password=root")
    cur = conx.cursor()
    query = """Select * from clientes where dni=%s"""
    try:    
        cur.execute(query,(dni,))
        fila = cur.fetchone()
        cliente = Cliente.Cliente(fila[0],fila[1],fila[2],fila[3])
        
    except:
        print("No existe ningun cliente con ese dni")
    cur.close()
    conx.commit()
    conx.close()
    return cliente
   
    
def buscarClientes():
    conx = psycopg2.connect("dbname=Polideportivo user=postgres password=root")
    cur = conx.cursor()
    query = """Select * from clientes"""
    clientes = []
    try:    
        cur.execute(query)
        while True:
            fila = cur.fetchone()
            if fila == None:
                break
            cliente = Cliente.Cliente(fila[0],fila[1],fila[2],fila[3])
            clientes.append(cliente)
    except:
        print("No existe ningun cliente")
    cur.close()
    conx.commit()
    conx.close()
    return clientes

def buscarDeportes():
    conx = psycopg2.connect("dbname=Polideportivo user=postgres password=root")
    cur = conx.cursor()
    query = """Select * from deportes"""
    deportes = []
    try:    
        cur.execute(query)
        while True:
            fila = cur.fetchone()
            if fila == None:
                break
            deporte = Deporte.Deporte(fila[0],fila[1])
            deportes.append(deporte)
    except:
        print("No existe ningun deporte")
    cur.close()
    conx.commit()
    conx.close()
    return deportes
    
def matricularCliente(dni,nombre,horario):
    conx = psycopg2.connect("dbname=Polideportivo user=postgres password=root")
    cur = conx.cursor()
    query = """INSERT INTO matriculas(horario, nombre, dni) VALUES(%s,%s,%s)"""
    cur.execute(query,(horario,nombre,dni))
    print("Se ha matriculado a "+dni+" en "+nombre+" correctamente")
    cur.close()
    conx.commit()
    conx.close()
    
def desmatricularCliente(dni,nombre,horario):
    conx = psycopg2.connect("dbname=Polideportivo user=postgres password=root")
    cur = conx.cursor()
    query = """DELETE from matriculas where horario=%s AND nombre=%s AND dni=%s"""
    cur.execute(query,(horario,nombre,dni))
    print("Se ha desmatriculado a "+dni+" en "+nombre+" correctamente")
    cur.close()
    conx.commit()
    conx.close()
    
def buscarDeportesPorCliente(cliente):
    conx = psycopg2.connect("dbname=Polideportivo user=postgres password=root")
    cur = conx.cursor()
    query = """Select D.nombre, precio from deportes D, matriculas M, clientes C WHERE D.nombre=M.nombre AND C.dni=M.dni """
    deportes = []
    try:    
        cur.execute(query)
        while True:
            fila = cur.fetchone()
            if fila == None:
                break
            deporte = Deporte.Deporte(fila[0],fila[1])
            deportes.append(deporte)
    except:
        print("No existe ningun deporte")
    cur.close()
    conx.commit()
    conx.close()
    return deportes
    