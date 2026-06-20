# = FUNCIONES =

def cabecera():
    """Muestra la cabecera de la aplicación"""
    titulo = r"""
      /$$$$$$                                           /$$$$$$$$                           
     /$$__  $$                                         |__  $$__/                           
    | $$  \__/  /$$$$$$  /$$$$$$/$$$$   /$$$$$$   /$$$$$$ | $$  /$$$$$$   /$$$$$$   /$$$$$$$
    | $$ /$$$$ |____  $$| $$_  $$_  $$ /$$__  $$ /$$__  $$| $$ |____  $$ /$$__  $$ /$$_____/
    | $$|_  $$  /$$$$$$$| $$ \ $$ \ $$| $$$$$$$$| $$  \__/| $$  /$$$$$$$| $$  \ $$|  $$$$$$ 
    | $$  \ $$ /$$__  $$| $$ | $$ | $$| $$_____/| $$      | $$ /$$__  $$| $$  | $$ \____  $$
    |  $$$$$$/|  $$$$$$$| $$ | $$ | $$|  $$$$$$$| $$      | $$|  $$$$$$$|  $$$$$$$ /$$$$$$$/
     \______/  \_______/|__/ |__/ |__/ \_______/|__/      |__/ \_______/ \____  $$|_______/ 
                                                                        /$$  \ $$          
                                                                       |  $$$$$$/          
                                                                        \______/                                                                                                   
                                👾 ¡Crea tu identidad gamer! 👾
    """
    print(titulo)

def crear_tag_basico(nombre):
    """
    Crea un gamertag básico usando las primeras 4 letras.
    
    Parámetro:
    nombre (str): El nombre del usuario.
    
    Return:
    str: Gamertag básico.
    """
    tag = nombre[:4]
    return tag
    
def crear_tag_invertido(nombre):
    """
    Crear un gamertag invirtiendo el nombre completo.
    
    Parámetro:
    nombre (str): El nombre del usuario.
    
    Return:
    str: Nombre invertido
    """
    tag = nombre[::-1]
    return tag

# - TAREA -
def crear_tag_intercalado(nombre, apellido):
    """
    Crea un gamertag intercalando la primera letra del nombre, con la primera letra del apellido
    y tomando el resto del nombre desde la posición uno seguido del resto del apellido desde la
    posición 1.
    
    Parámetro:
    nombre (str): El nombre del usuario.
    apellido (str): El apellido del usuario.
    
    Return:
    str: Nombre intercalado
    """
    tag = nombre[0] + apellido[0] + nombre[1:] + apellido[1:]
    return tag

def crear_tag_elite(nombre):
    """
    Crear un gamertag que toma las primeras 2 etras y las últimas 2 letras del nombre.
    
    Parámetro:
    nombre (str): El nombre del usuario.
    
    Return:
    str: Tag elite
    """
    tag = nombre[0:2] + nombre[-2:]
    return tag

def crear_tag_con_numero(nombre, numero_fav):
    """
    Crea un gamertag combinando las 1ras 5 letras del nombre con el # favorito.
    
    Parámetro:
    nombre (str): El nombre del usuario.
    numero_fav (int): El # fav. del usuario.
    
    Return:
    str: Tag con número
    """
    tag = nombre[0:5] + str(numero_fav)
    return tag

def mostrar_estadisticas(nombre):
    """
    Muestra estadísticas sobre el nombre del usuario.
    
    Parámetro:
    nombre (str): El nombre del usuario.
    
    Return: 
    str: Nombre completo
    int: Longitud del nombre
    str: Primera letra del nombre
    str: última letra del nombre
    """
    print("\n= ESTADÍSTICAS DE TU NOMBRE =")
    print(f"Nombre completo: {nombre}")
    print(f"Longitud del nombre: {len(nombre)}")
    print(f"Primera letra: {nombre[0]}")
    print(f"Última letra: {nombre[-1]}")
    print("\n")
    
def generar_todas_opciones(nombre, apellido, numero):
    """
    Genera y muestra todas las opciones de gamertags.
    
    Parámetros:
    Parámetro:
    nombre (str): El nombre del usuario.
    apellido (str): El apellido del usuario.
    numero (int): El # fav. del usuario.
    
    Retorna:
    None (imprime directamente)
    """
    print("\n=================================")
    print("TUS OPCIONES DE GAMERTAG:")
    print("=================================")
    
    print("\n1. TAG BÁSICO:", crear_tag_basico(nombre))
    print("\n2. TAG INVERTIDO:", crear_tag_invertido(nombre))
    print("\n3. TAG INTERCALADO:", crear_tag_intercalado(nombre, apellido))
    print("\n4. TAG ELITE:", crear_tag_elite(nombre))
    print("\n5. TAG CON NÚMERO:", crear_tag_con_numero(nombre, numero), "\n")

# = MAIN =
cabecera()

#Solicitar datos al usuario
nombre = input("\nIntroduce tu nombre: ")
apellido = input("\nIntroduce tu apellido: ")
numero = input("\nIntroduce tu número favorito: ")

mostrar_estadisticas(nombre)

generar_todas_opciones(nombre, apellido, numero)
print("\n¡Elige tu favorito y conquista el mundo gamer!\n")

#print("Tag básico:", crear_tag_basico(nombre))
#print("\nTag invertido:", crear_tag_invertido(nombre))
#print("\nTag intercalado:", crear_tag_intercalado(nombre, apellido))
#print("\nTag elite:", crear_tag_elite(nombre))
#print("\nTag con número favorito:", crear_tag_con_numero(nombre, numero), "\n")
