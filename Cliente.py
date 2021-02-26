'''
Created on 10 feb. 2021

@author: Ivi
'''
import RellenarTablas
import Deporte
class Cliente:  
    def __init__(self, nombre, dni, fnac, telefono):
        self.nombre=nombre
        self.dni=dni
        self.fnac=fnac
        self.telefono=telefono
        
    def __datos__(self):
        print(self.nombre, self.dni, self.fnac, self.telefono)
    
    def __deportes__(self):
        #deporte = RellenarTablas.clienteDeportes(self.dni)
        deportes = RellenarTablas.buscarDeportesPorCliente(self)
        print("El cliente "+self.nombre+" esta matriculado en los siguientes deportes")
        for depor in deportes:
            depor.__datos__()  