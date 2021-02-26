'''
Created on 16 feb. 2021

@author: Ivan
'''
class Deporte:  
    def __init__(self, nombre, precio):
        self.nombre=nombre
        self.precio=precio
        
    def __datos__(self):
        print(self.nombre, self.precio)
     