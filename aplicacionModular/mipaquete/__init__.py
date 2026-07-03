#Aquí va el código de inicialización.
#Es el código que se ejeutará cada vez que importemos cualquier cosa que se
#encuentre dentro del paquete

#Este archivo es obligatorio en paquetes para versiones de python menores a la 3.3

print("Se ha importado un módulo del paquete 'mipaquete'")

#Lista de módulos que queremos que se importen cuando el usuario haga un import * (import all)
__all__ = [
    'mimodulo2',
    'mimodulo3'   
]