# ===========================================
# CALCULADORA DE FITNESS Y SALUD PERSONAL
# ===========================================

def calcular_imc(peso_kg,altura_m):
    """
    Calcula el Índice de masa corporal (IMC).
    
    Fórmula: IMC = peso / (altura^2)
    
    Parámetros:
    peso_kg (float): Peso en kg.
    altura_m (float): Altura en metros.
    
    Return:
    float: El IMC calculado.
    """
    imc = peso_kg / (altura_m ** 2)
    return imc

def es_peso_saludable(imc):
    """
    Determina si el IMC está en rango saludable (18.5 - 24.9)
    
    Parámetro:
    imc (float): Índice de masa corporal.
    
    Return:
    bool: True si está en rango saludable, False si no.
    """
    #Operadores de comparación y lógicos
    return imc >= 18.5 and imc <= 24.9

def tiene_sobrepeso(imc):
    """
    Verifica si la persona tiene sobrepeso (imc >= 25)
    
    Parámetro:
    imc (float): El Índice de Masa Corporal calculado
    
    Return:
    True si hay sobrepeso (IMC ≥ 25)
    False si no hay sobrepeso (IMC < 25)
    """
    return imc >= 25.0

def tiene_bajo_peso(imc):
    """
    Determina si una persona tiene bajo peso según su IMC (imc < 18.5)
    
    Parámetro:
    imc (float): El Índice de Masa Corporal calculado
    
    Return:
    True si hay bajo peso (IMC < 18.5)
    False si no hay bajo peso (IMC ≥ 18.5)
    """
    return imc < 18.5

def calcular_calorias_diarias(peso_kg, altura_cm, edad, es_hombre):
    #True = 1 y False = 0
    """
    Calcula las calorías diarias recomendadas usando la Fórmula de Harris-Benedict.
    
    Fórmulas:
    Para hombres: 88.362 + (13.397 * peso) + (4.799 * altura) - (5.677 * edad)
    Para mujeres: 447.593 + (9.247 * peso) + (3.098 * altura) - (4.330 * edad)
    
    Parámetros:
    peso_kg (float): Peso en kilogramos
    altura_cm (float): Altura en centímetros
    edad (int): Edad en años
    es_hombre (bool): True si es hombre, False si es mujer
    
    Return: 
    (float): Las calorías diarias calculadas según el sexo
    """
    calorias_hombre = 88.362 + (13.397 * peso_kg) + (4.799 * altura_cm) - (5.677 * edad)
    calorias_mujer = 447.593 + (9.247 * peso_kg) + (3.098 * altura_cm) - (4.330 * edad)
    
    return es_hombre * calorias_hombre + (1 - es_hombre) * calorias_mujer

def calcular_agua_diaria(peso_kg):
    """
    Calcula los litros de agua recomendados al día.
    Se recomienda beber 35 mililitros de agua por cada kilogramo de peso corporal.
    
    Parámetro:
    peso_kg (float): Peso en kilogramos

    Return:
    (float): Litros de agua recomendados
    """
    litros_agua = (peso_kg * 35) / 1000
    return litros_agua

def calcular_ritmo_cardiaco_maximo(edad):
    """
    Calcula el ritmo cardíaco máximo recomendado durante ejercicio.
    
    Fórmula: 220 - edad
    
    Parámetro:
    edad (int): Edad en años

    Return:
    (int): Pulsaciones por minuto máximas recomendadas (ppm)
    """
    return 220 - edad

def generar_reporte_completo(nombre, peso, altura, edad, es_hombre):
    """
    Genera un reporte completo de salud y fitness.
    """
    print("=" * 60)
    print(f"REPORTE DE FITNESS Y SALUD - {nombre}")
    print("=" * 60)
    
    #Cálculos
    imc = calcular_imc(peso, altura)
    calorias = calcular_calorias_diarias(peso, altura*100, edad, es_hombre)
    agua = calcular_agua_diaria(peso)
    fc_max = calcular_ritmo_cardiaco_maximo(edad)
    
    #Información básica
    print(f"\nDatos personales:")
    print(f"    Peso: {peso} kg")
    print(f"    Altura: {altura} m")
    print(f"    Edad: {edad} años")
    print(f"    ¿Hombre?: {es_hombre}")
    
    #IMC y evaluación
    print(f"\nÍndice de masa corporal (IMC):")
    print(f"    Tu IMC: {round(imc, 2)}")
    print(f"    ¿Peso saludable? {es_peso_saludable(imc)}")
    print(f"    ¿Sobre peso? {tiene_sobrepeso(imc)}")
    print(f"    ¿Bajo peso? {tiene_bajo_peso(imc)}")
    
    #Calorias
    print(f"\n Nutrición:")
    print(f"   Calorías diarias recomendadas: {round(calorias, 0)} kcal")
    print(f"   Agua diaria recomendada: {round(agua, 2)} litros")
    
    #Cardio
    print(f"\nZona cardiaca:")
    print(f"   Frecuencia cardiaca máxima: {fc_max} ppm")
    print(f"   Zona de cardio óptima: {round(fc_max*0.6, 0)} - {round(fc_max*0.8, 0)} ppm")
    
    print("\n" + "="*60)

# ========================
#         Main
# ========================

cabecera = """
╔════════════════════════════════════════════════════════════╗
║     💪 CALCULADORA DE FITNESS Y SALUD PERSONAL 💪         ║
║                                                            ║
║        ¡Descubre tus métricas de salud óptimas!            ║
╚════════════════════════════════════════════════════════════╝
"""
print(cabecera)

#Solicitar los datos al usuario
nombre = input("\n¿Cuál es tu nombre?:")
peso = float(input("\n¿Cuánto pesas? (kg):"))
altura = float(input("\n¿Cuánto mides? (metros):"))
edad = int(input("\n¿Cuántos años tienes?:"))
sexo = input("\n¿Eres hombre o mujer? (H/M):")

#Convertir sexo a booleano
es_hombre = sexo == "H" or sexo == "h" or sexo == "hombre"

#Generar reporte
generar_reporte_completo(nombre, peso, altura, edad, es_hombre)

print("\n¡Cuida tu salud!")