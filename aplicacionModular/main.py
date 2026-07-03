# === CLASE SOBRE MÓDULOS ===

#Para importar directamente el objeto del módulo para tenerlo dentro del namespace global de este archivo y no tener que hacer mimodulo.funcion a cada rato.
#from mimodulo import funcion, Coche

#Hace lo mismo pero es para jalar todos los objetos del archivo del módulo y no uno en específico
#from mimodulo import * 

#El alias es para evitar colisiones de nombres entre el nombre del módulo y vars que hayamos definido, aunque también sirve para no tener que escribir toodo el nombre del módulo cada vez que se use
#from mimodulo import funcion as funcion2

#def funcion(arg):
#    print("Soy la funcion del main")
#    print(arg)

#if __name__ == '__main__':
#    funcion("Adios xd")
#    funcion2("Brrr")


# === CLASE SOBRE PAQUETES ===
from mipaquete import *

if __name__ == '__main__':
    mimodulo2.funcion_mimodulo2()
    mimodulo3.func_mimodulo3()