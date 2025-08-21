#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Física Computacional - Fundamentos de Python
Temas: Variables, Tipos de Datos, Operadores y Estructuras Básicas
"""

# =============================================================================
# 1. DEFINICIÓN FORMAL DE VARIABLE
# =============================================================================
print("\n" + "="*60)
print("1. DEFINICIÓN DE VARIABLE")
print("="*60)

"""
DEFINICIÓN:
"Una variable es un nombre que referencia a un valor almacenado en la memoria 
de la computadora. Este valor puede modificarse durante la ejecución del programa.
En Python, las variables son dinámicas (no requieren declaración de tipo) y 
actúan como etiquetas para objetos en memoria."
"""

# Ejemplo práctico:
print("\n--- 1.1 Variables como referencias ---")
variable_ejemplo = 10
print(f"Valor inicial: {variable_ejemplo} | Tipo: {type(variable_ejemplo)} | ID memoria: {id(variable_ejemplo)}")

variable_ejemplo = "Ahora soy string"
print(f"Nuevo valor: {variable_ejemplo} | Tipo: {type(variable_ejemplo)} | Nuevo ID: {id(variable_ejemplo)}")

# =============================================================================
# 2. CONVERSIONES ENTRE TIPOS
# =============================================================================
print("\n" + "="*60)
print("2. CONVERSIONES ENTRE TIPOS DE DATOS")
print("="*60)

variable_int = 1
print(f"Entero: {variable_int} es {type(variable_int)}")

variable_flt = float(variable_int) 
print(f"Flotante: {variable_flt} es {type(variable_flt)}")

variable_str = str(variable_int) 
print(f"String: '{variable_str}' es {type(variable_str)}")

variable_bool = bool(variable_int) 
print(f"Booleano (1): {variable_bool} es {type(variable_bool)}")

variable_bool = bool(0) 
print(f"Booleano (0): {variable_bool} es {type(variable_bool)}")

# =============================================================================
# 3. DOCUMENTACIÓN Y AYUDA
# =============================================================================
print("\n" + "="*60)
print("3. DOCUMENTACIÓN DE FUNCIONES")
print("="*60)

print("Documentación de bool():")
print("-" * 40)
print(bool.__doc__[:200] + "...")  # Mostrar solo primeros 200 caracteres
print("-" * 40)
print("\nPara ayuda completa usar: help(bool)")

# =============================================================================
# 4. REFERENCIAS Y ALIASING
# =============================================================================
print("\n" + "="*60)
print("4. REFERENCIAS Y ALIASING")
print("="*60)

a = [1, 2, 3]
b = a  # 'b' referencia al MISMO objeto que 'a'
print(f"Antes: a = {a}, b = {b}")
print(f"Mismo objeto? {a is b} | Mismo ID? {id(a) == id(b)}")

b.append(4)
print(f"Después de b.append(4): a = {a}")  # ¡Se modificó también 'a'!

# =============================================================================
# 5. CONVENCIONES DE NOMBRES
# =============================================================================
print("\n" + "="*60)
print("5. CONVENCIONES DE NOMBRES (PEP 8)")
print("="*60)

"""
Reglas para nombres de variables:
1. Pueden contener letras, números y _
2. No pueden empezar con número
3. Distingue mayúsculas/minúsculas
4. No usar palabras reservadas (if, for, etc.)
"""

nombre_válido = "snake_case"  # Estilo recomendado
_NombreConCamelCase = "no recomendado en Python"
CONSTANTE = "MAYÚSCULAS para constantes"

print(f"snake_case: {nombre_válido}")
print(f"CamelCase (no recomendado): {_NombreConCamelCase}")
print(f"CONSTANTE: {CONSTANTE}")

# =============================================================================
# 6. OPERADORES DE ASIGNACIÓN
# =============================================================================
print("\n" + "="*60)
print("6. OPERADORES DE ASIGNACIÓN")
print("="*60)

# Asignación simple
x = 10
print(f"Asignación simple: x = {x}")

# Asignación múltiple
a, b, c = "uno", 2, False
print(f"Asignación múltiple: a='{a}', b={b}, c={c}")

# Asignación aumentada
print(f"\nAntes de x += 5: x = {x}")
x += 5  # Equivale a x = x + 5
print(f"Después de x += 5: x = {x}")

# Intercambio de valores
print(f"\nAntes intercambio: a='{a}', b={b}")
a, b = b, a
print(f"Después intercambio: a={a}, b='{b}'")

# =============================================================================
# 7. MANIPULACIÓN DE CADENAS (STRINGS)
# =============================================================================
print("\n" + "="*60)
print("7. MANIPULACIÓN DE CADENAS")
print("="*60)

name_file = "Kepler's-Problem"
position = 10

print(f"Cadena original: '{name_file}'")
print(f"Carácter en posición {position}: '{name_file[position]}'")
print(f"Desde inicio hasta posición {position}: '{name_file[:position]}'")
print(f"Desde posición {position} hasta final: '{name_file[position:]}'")
print(f"Desde posición 3 hasta {position}: '{name_file[3:position]}'")
print(f"Longitud de la cadena: {len(name_file)} caracteres")

# =============================================================================
# 8. CONSTRUCCIÓN DE NOMBRES DE ARCHIVO
# =============================================================================
print("\n" + "="*60)
print("8. CONSTRUCCIÓN DE NOMBRES DE ARCHIVO")
print("="*60)

x_init = 10.55
px_init = 0.5

# Construcción con reemplazo de puntos por guiones bajos
name_file = "Kepler's-Problem-" + str(x_init).replace('.','_')
name_file += '-'
name_file += str(px_init).replace('.','_')
name_file += '.txt'

print(f"Nombre de archivo construido: {name_file}")

# División de cadenas
partes = name_file.split('.')
print(f"Split por '.': {partes}, el tipo de la variable partes es: {type(partes)}")

# =============================================================================
# 9. LISTAS EN PYTHON
# =============================================================================
print("\n" + "="*60)
print("9. LISTAS EN PYTHON")
print("="*60)

# Las listas en python se definen con []
x_init = [2.1, 3.1, 4.4, 4.52, 56.12, 40.9, 4.1]
print(f'La lista "x_init" es: {x_init}')
print(f'El número de elementos de "x_init" es: {len(x_init)}')
print(f'Slice [2:5]: {x_init[2:5]}')

# Las listas son mutables
x_init[2] = name_file
print(f'Después de modificar índice 2: {x_init}')

# =============================================================================
# 10. TUPLAS EN PYTHON
# =============================================================================
print("\n" + "="*60)
print("10. TUPLAS EN PYTHON")
print("="*60)

# Las tuplas en python se definen con ()
x_init = (2.1, 3.1, 4.4, 4.52, 56.12, 40.9, 4.1)
print(f'La variable "x_init" es del tipo {type(x_init)} y es: {x_init}')
print(f'Slice [2:5]: {x_init[2:5]}')

# Conversión entre listas y tuplas
print("\n--- Conversión entre listas y tuplas ---")
lista_from_tupla = list(x_init)
tupla_from_lista = tuple(lista_from_tupla)
print(f'Lista desde tupla: {lista_from_tupla}')
print(f'Tupla desde lista: {tupla_from_lista}')

# =============================================================================
# 11. OPERACIONES CON LISTAS
# =============================================================================
print("\n" + "="*60)
print("11. OPERACIONES CON LISTAS")
print("="*60)

x_init = list(x_init)  # Convertir a lista para modificar

# Append - agregar elemento al final
x_init.append(True)
print(f'Después de append(True): {x_init}')

# Pop - eliminar último elemento
x_init.pop()
print(f'Después de pop(): {x_init}')

# Pop con índice - eliminar elemento específico
x_init.pop(0)
print(f'Después de pop(0): {x_init}')

# Remove - eliminar por valor (primer ocurrencia)
if 56.12 in x_init:
    x_init.remove(56.12)
    print(f'Después de remove(56.12): {x_init}')

# =============================================================================
# 12. OPERACIONES ARITMÉTICAS
# =============================================================================
print("\n" + "="*60)
print("12. OPERACIONES ARITMÉTICAS")
print("="*60)

print(60*"*")
print("Operaciones aritméticas básicas:")
print(f'Suma: 0.1 + 0.2 = {0.1 + 0.2}')
print(f'Módulo: 4 % 3 = {4 % 3}')
print(f'Potencia: 2**6 = {2**6}')
print(60*"*")

# =============================================================================
# 13. OPERADORES DE COMPARACIÓN
# =============================================================================
print("\n" + "="*60)
print("13. OPERADORES DE COMPARACIÓN")
print("="*60)

print("Operadores de comparación (devuelven booleanos):")
print(f'2 < 6 = {2 < 6} | Tipo: {type(2 < 6)}')
print(f'9 <= 9 = {9 <= 9} | Tipo: {type(9 <= 9)}')
print(f'9 == 7 = {9 == 7} | Tipo: {type(9 == 7)}')
print(f'9 != 7 = {9 != 7} | Tipo: {type(9 != 7)}')
print(f'5 > 3 = {5 > 3} | Tipo: {type(5 > 3)}')

# =============================================================================
# 14. OPERADORES LÓGICOS
# =============================================================================
print("\n" + "="*60)
print("14. OPERADORES LÓGICOS")
print("="*60)

print("Operadores lógicos con booleanos:")
print(f'AND: True and False -> {True and False}')
print(f'OR: False or False -> {False or False}')
print(f'NOT: not True -> {not True}')
print(f'Combinación: (5 > 3) and (2 < 4) -> {(5 > 3) and (2 < 4)}')

# =============================================================================
# 15. EJERCICIOS PRÁCTICOS DE FÍSICA
# =============================================================================
print("\n" + "="*60)
print("15. EJERCICIOS PRÁCTICOS DE FÍSICA")
print("="*60)

# Ejercicio 1: Conversión de unidades
print("\n--- Ejercicio 1: Conversión de unidades ---")
temperatura_c = 25.0
temperatura_k = temperatura_c + 273.15
print(f"{temperatura_c}°C = {temperatura_k} K")

# Ejercicio 2: Cálculo de energía cinética
print("\n--- Ejercicio 2: Energía cinética ---")
masa = 2.5  # kg
velocidad = 10.0  # m/s
energia_cinetica = 0.5 * masa * velocidad**2
print(f"Energía cinética: {energia_cinetica} Joules")

# Ejercicio 3: Análisis de datos experimentales
print("\n--- Ejercicio 3: Análisis de datos ---")
datos_experimento = [12.3, 15.7, 8.9, 22.1, 18.4, 9.8]
print(f"Datos experimentales: {datos_experimento}")

# Calcular promedio
promedio = sum(datos_experimento) / len(datos_experimento)
print(f"Promedio: {promedio:.2f}")

# Encontrar valor máximo y mínimo
maximo = max(datos_experimento)
minimo = min(datos_experimento)
print(f"Valor máximo: {maximo}")
print(f"Valor mínimo: {minimo}")

# =============================================================================
# EJECUCIÓN PRINCIPAL
# =============================================================================
if __name__ == "__main__":
    print("\n" + "="*60)
    print("¡CLASE COMPLETADA!")
    print("="*60)
    print("\nResumen de temas cubiertos:")
    temas = [
        "1. Definición de variables",
        "2. Conversiones entre tipos", 
        "3. Documentación de funciones",
        "4. Referencias y aliasing",
        "5. Convenciones de nombres",
        "6. Operadores de asignación",
        "7. Manipulación de cadenas",
        "8. Construcción de nombres de archivo",
        "9. Listas y operaciones",
        "10. Tuplas e inmutabilidad",
        "11. Operaciones con listas",
        "12. Operaciones aritméticas",
        "13. Operadores de comparación",
        "14. Operadores lógicos",
        "15. Ejercicios prácticos de física"
    ]
    for i, tema in enumerate(temas, 1):
        print(f"  {i:2d}. {tema}")
    
    print("\n" + "="*60)
    print("¡Próxima clase: Control de flujo (if, while, for)!")
    print("="*60)
