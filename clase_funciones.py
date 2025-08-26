#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Física Computacional - Funciones en Python
Temas: Definición, parámetros, retorno, alcance y documentación
"""

from misFunciones import isPrime

# =============================================================================
# 1. DEFINICIÓN BÁSICA DE FUNCIONES
# =============================================================================
print("\n" + "="*60)
print("1. DEFINICIÓN BÁSICA DE FUNCIONES")
print("="*60)

def hola():
    """Función que imprime un saludo básico."""
    print("Hola mundo")

# Llamada a la función
print("Llamando a la función hola():")
hola()

# =============================================================================
# 2. FUNCIONES CON PARÁMETROS
# =============================================================================
print("\n" + "="*60)
print("2. FUNCIONES CON PARÁMETROS")
print("="*60)

def hola_nombre(nombre: str):
    """
    Función que saluda a una persona específica.
    
    Args:
        nombre (str): Nombre de la persona a saludar
    """
    print(f"\t Variable global: {mi_nombre}")
    print(f"\t Variable local (parámetro): {nombre}")
    print(f"Hola mundo {nombre}")

# Variable global
mi_nombre = 'Pedro'

print("Llamando a la función con parámetro:")
hola_nombre(mi_nombre)

# Demostración de alcance
print(f"\nVariable global fuera de función: {mi_nombre}")
# print(f"Variable local fuera de función: {nombre}")  # Esto daría error

# =============================================================================
# 3. FUNCIONES CON RETORNO Y TYPE HINTS
# =============================================================================
print("\n" + "="*60)
print("3. FUNCIONES CON RETORNO Y TYPE HINTS")
print("="*60)

def mi_suma(sumando1: float, sumando2: float) -> float:
    """
    Calcula la suma del primer argumento más tres veces el segundo.
    
    Args:
        sumando1 (float): Primer valor a sumar
        sumando2 (float): Segundo valor (se multiplica por 3)
        
    Returns:
        float: Resultado de sumando1 + 3 * sumando2
        
    Example:
        >>> mi_suma(2.0, 3.0)
        11.0
    """
    resultado = sumando1 + 3 * sumando2
    return resultado

# Uso de la función con type hints
x_init, y_init = 10.3, 2.0
mi_resultado = mi_suma(x_init, y_init)

print(f"El resultado de {x_init} + 3*{y_init} es {mi_resultado}")

# =============================================================================
# 4. DOCSTRINGS Y DOCUMENTACIÓN
# =============================================================================
print("\n" + "="*60)
print("4. DOCSTRINGS Y DOCUMENTACIÓN")
print("="*60)

print("Revisando el docstring de la función:")
print("-" * 40)
print(mi_suma.__doc__)
print("-" * 40)

# También se puede usar help()
print("\nUsando help():")
print("-" * 40)
# help(mi_suma)  # Descomentar para ver ayuda completa
print("(help(mi_suma) mostraría información detallada)")
print("-" * 40)

# =============================================================================
# 5. FUNCIÓN EXTERNA (SIMULACIÓN)
# =============================================================================
print("\n" + "="*60)
print("5. FUNCIÓN EXTERNA - SIMULACIÓN")
print("="*60)

# Probando la función isPrime
number = 143
resultado = isPrime(number)

print(f"¿El número {number} es primo? {resultado}")
exit()
# Probamos con más números para demostración
print("\nVerificación de primos para varios números:")
numeros_prueba = [2, 3, 4, 17, 25, 29, 143, 1000]

for num in numeros_prueba:
    es_primo = isPrime(num)
    print(f"  {num}: {'Sí' if es_primo else 'No'} es primo")

# =============================================================================
# 6. EJERCICIOS PRÁCTICOS DE FÍSICA
# =============================================================================
print("\n" + "="*60)
print("6. EJERCICIOS PRÁCTICOS DE FÍSICA")
print("="*60)

# =============================================================================
# 7. BUENAS PRÁCTICAS Y CONVENCIONES
# =============================================================================
print("\n" + "="*60)
print("7. BUENAS PRÁCTICAS Y CONVENCIONES")
print("="*60)

print("Convenciones recomendadas:")
print("  Nombres de funciones en snake_case: mi_funcion")
print("  Type hints para parámetros y retorno")
print("  Docstrings completos con Args, Returns, Examples")
print("  Variables locales con nombres descriptivos")
print("  Funciones cortas y con un solo propósito")

# =============================================================================
# EJECUCIÓN PRINCIPAL
# =============================================================================
if __name__ == "__main__":
    print("\n" + "="*60)
    print("¡CLASE DE FUNCIONES COMPLETADA!")
    print("="*60)
    print("\nResumen de temas cubiertos:")
    temas = [
        "1. Definición básica de funciones",
        "2. Funciones con parámetros y alcance",
        "3. Funciones con retorno y type hints", 
        "4. Docstrings y documentación",
        "5. Uso de funciones externas",
        "6. Ejercicios prácticos de física",
        "7. Buenas prácticas y convenciones"
    ]
    for i, tema in enumerate(temas, 1):
        print(f"  {i}. {tema}")
    
    print("\n" + "="*60)
    print("¡Próxima clase: Módulos y manejo de excepciones!")
    print("="*60)
