'''
Created on 23 ene. 2021

@author: Ivan
'''

import CreacionTablas
import RellenarTablas
import EntradaSalida
import Funciones

print("Creamos las tablas")
CreacionTablas.creacionTablas()

print("")

print("Rellenamos la tabla Deportes")
RellenarTablas.rellenarDeportes()

opcion=0
while opcion != 7:
    print("")
    print("============================MENU============================")
    opcion = EntradaSalida.imprimirMenu()

    if opcion == 1:
        Funciones.altaCliente()
    elif opcion == 2:
        Funciones.bajaCliente()
    elif opcion == 3:
        Funciones.mostrarDatos()
    elif opcion == 4:
        Funciones.matricular()
    elif opcion == 5:
        Funciones.desmatricular()
    elif opcion == 6:
        Funciones.mostrarDeportes()
    elif opcion == 7:
        Funciones.salir()
    else:
       Funciones.invalido()
