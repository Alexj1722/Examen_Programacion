#-*-coding: utf-8 -*-
import sys
import platform
from Datos import datos

class ingreso:
    """Se encarga de ingresar los autos"""
    def __init__(self):
        """Inicializa un ingreso vacio"""
        self.registrados = list()
        
        def Nuevo_Vehiculo(self, numero="",marca="",modelo="",tipo="",hora="",estado="",horas=""):
            """Registra un vehiculo ingresado en el programa"""
            self.registrados.append(datos(numero, marca, modelo, tipo, hora, estado, horas))
            
        def Buscar_Vehiculo(self, Placa):
            """Buscar un vehiculo por su numero de placa"""
            for vehiculo in self.registrados:
                if str(vehiculo.numero) == str(Placa):
                    return vehiculo
        return None
            
        