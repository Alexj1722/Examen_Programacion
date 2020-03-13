#-*-coding: utf-8 -*-
#Programa: Examen.py
#objetivo: desarrollo de ejercicio de examen
#Autor: Alex Mendoza
#Fecha: 23/03/2020
import sys
import platform
from datetime import datetime, timedelta
from Agregar import ingreso


class Menu:
    """Inicio del programa"""
    def __init__(self):
        """inicializa el programa"""
        self.Autos = ingreso()
    def seleccion_Opcion(self):
        """Asignacion de los parametros a las variables"""
        self.opciones={"1": self.Ingresar_Vehiculo,
                       "2": self.Eliminar_Vehiculo,
                       "3": self.Listado_Vechiculos,
                       "4": self.Buscar_Vehiculo,
                       "5": self.Salir}
                    
    def desplazar_Menu(self):
        """Desplaza el menu pidiendo los datos de los vehiculos que van ingresando"""
        print("""1. Ingresar un vehiculo
                2. Eliminar un vehiculo
                3. Mostrar el listado de vehiculos rgistrados
                4. Buscar vehiculo por numero de placa
                5. Salir""")
        
    def Ingresar_Vehiculo(self):
        """Agrega un Nuevo Vehiculo"""
        Numero_Placa = int(input("Ingrese el numero de placa del vehiculo: "))
        Marca = input("Ingrese la marca de vehiculo: ") 
        Modelo = input("Ingrese el modelo de vehiculo: ")
        Tipo =input ("Ingrese tipo de vehiculo: Motocicleta o Automovil")
        if Tipo != "Automovil" or Tipo != "Motocicleta":
            print("Escriba bien el tipo de vehiculo porfavor")
        Hora_Ingreso = datetime.date.now()
        Estado = True
        Horas = int(input("Ingrese cuanto tiempo estara en horas cerradas:  "))
        if Horas > 1 and Tipo == "Automovil":
           total = (Horas-1 + (Horas-1)(0.20))+20
        elif Horas > 1 and Tipo == "Motocicleta":
            total = (Horas-1 + (Horas-1)(0.10))+10
        elif Horas >5:
            print("No puede estar mas de 5 horas aqui...")
        self.Autos.Nuevo_Vehiculo(Numero_Placa, Marca, Modelo, Tipo,Hora_Ingreso, Estado, Horas)
        print("Nuevo Vehiculo Agregado")
        print("El total a pagar es de {0}".format(total))
        print("LA hora de salida del vehiculo es {0}".format(datetime.now() + timedelta(hours=Horas)))
        
        ingreso
    def Eliminar_Vehiculo(self, filter):
        """Eliminar un vehiculo"""
        filter = input("Ingrese placa del vehiculo que desea eliminar: ")
        self.Autos.pop(int(filter))
        
    def Listado_Vechiculos(self):
        """Lista los vehiculos regisrados en el sistema"""
        pass 
    
    def Buscar_Vehiculo(self):
        """Busca un vehiculo por su numero de placa"""
        pass
    
    
    def Salir(self):
        """Sale del programa"""
        sys.exit(0)        
        
        
    def Run(self):
        """Metodo de entrada para el programa"""
        while True:
            self.desplazar_Menu()
            seleccion = int(input("Seleccione lo que desea Hacer:  "))
            accion = self.opciones.get(seleccion)
            if accion:
                accion()
            else:
                print("Opcion {0} no valida".format(seleccion))
            
                    
        
if __name__ == "__main__":
    menu = Menu()
    menu.Run()