"""
POO: Es un paradigma de programacion que se basa en el concepto de "objetos", los cuales son entidades que combinan datos
(llamados atributos) y funciones (llamadas metodos) que operan sobre esos datos.
Objeto: Es una instancia de una clase.
Atributos: Son caracteristicas o propiedades que describen el estado de un objeto.
Metodos: Funciones o procedimientos asociados a un objeto que definen su comportamiento o las acciones que puede realizar.
Clase: Un modelo o plantilla que define la estructura y comportamiento de los objetos.
"""

class Auto:
    marca = None
    modelo = None
    anio = None
    color = None

    def encendido(self): # self: se refiere al objeto que esta usando este metodo
        print('El auto esta Encendido!')
        
    def apagado(self): # self: se refiere al objeto que esta usando este metodo
        print('El auto esta Apagado!')
    