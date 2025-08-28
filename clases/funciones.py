#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Física Computacional - Funciones en Python
Temas: Definición, parámetros, retorno, alcance, documentación y manejo de errores
"""

from misFunciones import *

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
# Probamos con más números para demostración
print("\nVerificación de primos para varios números:")
numeros_prueba = [2, 3, 4, 17, 25, 29, 143, 1000]

for num in numeros_prueba:
    es_primo = isPrime(num)
    print(f"  {num}: {'Sí' if es_primo else 'No'} es primo")

print("\n" + 60*"*")
print(f'Factorial de 0 es {myFactorial(0)}')
print(f'Factorial de 1 es {myFactorial(1)}')
print(f'Factorial de 5 es {myFactorial(5)}')
print(f'Factorial de -1 es {myFactorial(-1)}')
print(f'Factorial de "5" es {myFactorial("5")}')


# =============================================================================
# 6. FUNCIONES CON MANEJO DE ERRORES
# =============================================================================

# 6.1 Funciones con parámetros múltiples
def greater_than(x, y):
    """Compara dos números e imprime cuál es mayor o si son iguales."""
    try:
        if x < y: 
            print(f'{y} es mayor que {x}')
        elif y < x:
            print(f'{x} es mayor que {y}')
        else:
            print(f'{x} es igual que {y}')
    except Exception as e:
        print("Error:", e)
    finally:
        print("Execution finished in greater_than\n")


# 6.2 Valores de parámetros predeterminados
def greater_than2(x, y=0):
    """Compara dos números, con y teniendo valor por defecto de 0."""
    try:
        if x < y: 
            print(f'{y} es mayor que {x}')
        elif y < x:
            print(f'{x} es mayor que {y}')
        else:
            print(f'{x} es igual que {y}')
    except Exception as e:
        print("Error:", e)
    finally:
        print("Execution finished in greater_than2\n")


# 6.3 Argumentos nombrados
def introduce(name, last_name):
    """Imprime un saludo con nombre y apellido."""
    try:
        if not isinstance(name, str) or not isinstance(last_name, str):
            raise TypeError(
                f'Los parámetros deben ser "str" y son {type(name).__name__} {type(last_name).__name__}'
            )
        print(f'Hola soy {name} {last_name}')
    except Exception as e:
        print("Error:", e)
    finally:
        print("Execution finished in introduce\n")


# 6.4 Argumentos arbitrarios (*args)
def list_numbers(*args):
    """Imprime todos los números pasados como argumentos."""
    try:
        for number in args:
            if not isinstance(number, (int, float)):
                raise ValueError("Todos los argumentos deben ser números")
            print("Número:", number)
    except Exception as e:
        print("Error:", e)
    finally:
        print("Execution finished in list_numbers\n")


# 6.5 Argumentos arbitrarios con palabras clave (**kwargs)
def show_info(**kwargs):
    """Imprime pares clave-valor de argumentos nombrados arbitrarios."""
    try:
        for key, value in kwargs.items():
            print(key, ":", value)
        if not kwargs:
            raise ValueError('Debe existir al menos un argumento con nombre')
    except Exception as e:
        print("Error:", e)
    finally:
        print("Execution finished in show_info\n")


# 6.6 Combinando todo
def my_function(name, last_name, *args, **kwargs):
    """Ejemplo combinando argumentos posicionales, arbitrarios y nombrados."""
    try:
        if not isinstance(name, str) or not isinstance(last_name, str):
            raise TypeError("name y last_name deben ser cadenas de texto")

        print("Name:", name, last_name)
        print("Extra args:", args)
        print("Keyword args:", kwargs)

        for arg in args:
            print("arg:", arg)
        for key in kwargs:
            print("key:", key, "has value:", kwargs[key])

    except Exception as e:
        print("Error:", e)
    finally:
        print("Execution finished in my_function\n")


# =============================================================================
# EJECUCIÓN PRINCIPAL
# =============================================================================
if __name__ == "__main__":
    print("\n" + "="*60)
    print("¡CLASE DE FUNCIONES COMPLETADA!")
    print("="*60)

    # Pruebas de la segunda parte
    print("\n" + 60*"*")
    greater_than(5, 3)
    greater_than(3, 5)
    greater_than("a", 2)
    greater_than(5, 5)

    print("\n" + 60*"*")
    greater_than2(5, "x")
    greater_than2(5, 2)

    print("\n" + 60*"*")
    introduce("Ada", "Lovelace")
    introduce("Ada", True)
    introduce(last_name="Einstein", name="Albert")
    introduce("Alan", 42)

    print("\n" + 60*"*")
    list_numbers(1, 2, 3)
    list_numbers(1, "b", 3)

    print("\n" + 60*"*")
    show_info(name="Isaac", last_name="Newton", field="Physics")
    show_info()

    print("\n" + 60*"*")
    my_function("Marie", "Curie", 1, 2, country="France", field="Chemistry")
    my_function(123, "Curie")

    print("\nResumen de temas cubiertos:")
    temas = [
        "1. Definición básica de funciones",
        "2. Funciones con parámetros y alcance",
        "3. Funciones con retorno y type hints", 
        "4. Docstrings y documentación",
        "5. Uso de funciones externas",
        "6. Funciones con manejo de errores",
    ]
    for i, tema in enumerate(temas, 1):
        print(f"  {i}. {tema}")
    
    print("\n" + "="*60)
    print("¡Próxima clase: Módulos y manejo de excepciones!")
    print("="*60)
