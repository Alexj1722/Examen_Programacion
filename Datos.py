#-*-coding: utf-8 -*-
import datetime

class datos:
    """Aqui se pediran los datos para los vehiculos"""
    def __init__(self, numero, marca,modelo,tipo,hora,estado, horas):
        """Inicializa la clase"""
        self.Numero = numero
        self.Marca = marca
        self.Modelo = modelo
        self.tipo = tipo
        self.hora = datetime.date.now()
        self.estado = True
        self.Horas = horas
        