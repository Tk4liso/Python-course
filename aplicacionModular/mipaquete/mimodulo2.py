def funcion_mimodulo2():
    print("Hola desde mipaquete (mimodulo 2)xd")

# === CLASE SOBRE __name__ ===
#El if __name__ == '__main__' sirve para que python sepa si el archivo/fichero actual se está ejecutando como "principal" y no como
#código importado. Si se ejecutase este archivo como código importado la variable __name__ sería igual a la ruta del fichero 
#(mipaquete.mimodulo2), pero cuando ejecutamos el archivo solito __name__ es igual a __main__.

#Entonces, ese if ayuda a que podamos ejecutar cierto código cuando ejecutamos el archivo de manera aislada pero no cuando lo ejecutamos
#como un archivo importado.

if __name__ == '__main__':
    funcion_mimodulo2()