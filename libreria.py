from libro import Libro


class Libreria:
    def __init__(self):
        self.__libros = []
    
    def agregar_final(self, libro:Libro):
        self.__libros.append(libro)

    def agregar_inicio(self, libro:Libro):
        self.__libros.insert(0, libro)

    def mostrar(self):
        for libro in self.__libros:
            print(libro)

l01 = Libro(id=1, origen_x=2, origen_y=3, destino_x=4, destino_y=5, velocidad=6, red=7, green=8, blue=9, distancia= "")
l02 = Libro("9", "10", "11", "12", "13", "14", "15", "16", "17", "")
libreria = Libreria()
libreria.agregar_final(l01)
libreria.agregar_inicio(l02)
libreria.agregar_inicio(l01)
libreria.mostrar()