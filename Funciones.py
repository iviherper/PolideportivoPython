'''
Created on 5 feb. 2021

@author: Ivan
'''
import CreacionTablas
import RellenarTablas
import EntradaSalida
import Cliente

def altaCliente():
    cliente = EntradaSalida.pedirCliente()
    cliente.__datos__()
    RellenarTablas.altaCliente(cliente)
    
def bajaCliente():
    dni = EntradaSalida.pedirDni()
    RellenarTablas.bajatCliente(dni)
    
def mostrarDatos():
    cuantos = EntradaSalida.pedirCuantos()
    if cuantos.lower() == "uno" :
        dni = EntradaSalida.pedirDni()
        cliente = RellenarTablas.buscarCliente(dni)
        cliente.__datos__()
    elif cuantos.lower() == "todos":
        clientes = RellenarTablas.buscarClientes()
        for cli in clientes:
            cli.__datos__()
    else:
        print("Debes introducir uno o todos")
        
def matricular():
    dni = EntradaSalida.pedirDni()
    #cliente = RellenarTablas.buscarCliente(dni)
    deportes = RellenarTablas.buscarDeportes()
    for depor in deportes:
        depor.__datos__()
    deporte = EntradaSalida.pedirDeporte()
    horario = EntradaSalida.pedirHorario()
    RellenarTablas.matricularCliente(dni, deporte, horario)
    
def desmatricular():
    dni = EntradaSalida.pedirDni()
    #cliente = RellenarTablas.buscarCliente(dni)
    deportes = RellenarTablas.buscarDeportes()
    for depor in deportes:
        depor.__datos__()
    deporte = EntradaSalida.pedirDeporte()
    horario = EntradaSalida.pedirHorario()
    RellenarTablas.desmatricularCliente(dni, deporte, horario)
    
def mostrarDeportes():
    dni = EntradaSalida.pedirDni()
    cliente = RellenarTablas.buscarCliente(dni)
    cliente.__deportes__()
    
def salir():
    print("Saliendo...")
    
def invalido():
    print ("Introduce un numero valido")
    
            