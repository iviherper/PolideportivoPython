'''
Created on 5 feb. 2021

@author: Ivan
'''
from Cliente import Cliente

def imprimirMenu():
    print("1. Dar de alta un cliente con sus datos personales")
    print("2. Dar de baja un cliente")
    print("3. Mostrar los datos personales de un cliente o de todos")
    print("4. Matricular a un cliente en un deporte")
    print("5. Desmatricular a un cliente en un deporte")
    print("6. Mostrar los deportes de un cliente")
    print("7. Salir")
    print()
    opcion = int (input("Introduce una opcion"))
    return opcion

def pedirCliente():
    nombre = input("Introduce el nombre del cliente")
    dni = input("Introduce el dni del cliente")
    fecnac = input("Introduce la fecha de nacimiento del cliente")
    telefono = int (input("Introduce el telefono del cliente"))
    cliente = Cliente(nombre,dni,fecnac,telefono)
    return cliente

def pedirDni():
    return input("Introduce el dni del cliente")

def pedirCuantos():
    return input("Desea ver los datos personales de un cliente o de todos?, uno / todos")

def pedirDeporte():
    return input("Introduce el nombre del deporte")

def pedirHorario():
    return input("Introduce el horario")