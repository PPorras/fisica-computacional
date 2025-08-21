#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Física Computacional - Control de Flujo en Python
Temas: Condicionales (if, elif, else) y Bucles (while, for)
"""

# =============================================================================
# 1. ESTRUCTURAS CONDICIONALES: if, elif, else
# =============================================================================
print("\n" + "="*60)
print("1. ESTRUCTURAS CONDICIONALES: if, elif, else")
print("="*60)

# Ejemplo 1: Clasificación de números
print("\n--- 1.1 Clasificación de números ---")
num = -1.0
print(f"Analizando el número: {num}")

if num > 0:
    print(f'{num} es positivo')
elif num < 0:
    print(f'{num} es negativo')
else:
    print(f'{num} es cero')

# =============================================================================
# 2. BUCLE WHILE
# =============================================================================
print("\n" + "="*60)
print("2. BUCLE WHILE")
print("="*60)

# Ejemplo 1: Contador básico
print("\n--- 2.1 Contador con while ---")
i = 0
while i < 10:
    print(f'Iteración {i + 1} del bucle while')
    i += 1  # i = i + 1

# Ejemplo 2: Simulación física (caída libre)
print("\n--- 2.2 Simulación de caída libre ---")
altura = 100.0  # metros
gravedad = 9.81  # m/s²
tiempo = 0.0

print(f"Simulación de caída desde {altura} metros")
while altura > 0:
    tiempo += 0.5  # incremento de tiempo en segundos
    altura = 100.0 - 0.5 * gravedad * tiempo**2
    if altura < 0:
        altura = 0.0
    print(f"Tiempo: {tiempo:.1f}s - Altura: {altura:.1f}m")

print(f"\n¡Impacto en el suelo a los {tiempo:.1f} segundos!")

# =============================================================================
# 3. BUCLE FOR
# =============================================================================
print("\n" + "="*60)
print("3. BUCLE FOR")
print("="*60)

# Ejemplo 1: Iteración sobre tupla
print("\n--- 3.1 Iteración sobre tupla ---")
numeros = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print(f"Tupla: {numeros}")

# Verificación de pertenencia
print(f"¿Está el número 100 en la tupla? {100 in numeros}")
print(f"¿Está el número 5 en la tupla? {5 in numeros}")

print("\nRecorriendo la tupla:")
for numero in numeros:
    print(f'Elemento: {numero}')

# Ejemplo 2: Uso de range()
print("\n--- 3.2 Uso de range() ---")
print("Números del 0 al 10:")
for numero in range(0, 11):
    print(f'Número: {numero}')

# Ejemplo 3: Range con paso (física - valores de tiempo)
print("\n--- 3.3 Range con paso (valores de tiempo) ---")
print("Tiempos de 0 a 10 segundos con incremento de 0.5:")
for tiempo in range(0, 21):  # 0 to 20 (para dividir entre 2)
    tiempo_segundos = tiempo / 2.0
    print(f'Tiempo: {tiempo_segundos:.1f}s')

# =============================================================================
# 4. EJERCICIOS PRÁCTICOS DE FÍSICA
# =============================================================================
print("\n" + "="*60)
print("4. EJERCICIOS PRÁCTICOS DE FÍSICA")
print("="*60)

# Ejercicio 1: Cálculo de posición con while
print("\n--- Ejercicio 1: Movimiento uniformemente acelerado ---")
posicion = 0.0
velocidad_inicial = 10.0  # m/s
aceleracion = 2.0  # m/s²
tiempo_simulacion = 0.0

print("Simulación de movimiento:")
while tiempo_simulacion <= 5.0:
    posicion = velocidad_inicial * tiempo_simulacion + 0.5 * aceleracion * tiempo_simulacion**2
    print(f"Tiempo: {tiempo_simulacion:.1f}s - Posición: {posicion:.1f}m")
    tiempo_simulacion += 1.0

# Ejercicio 2: Tabla de conversión temperatura con for
print("\n--- Ejercicio 2: Conversión Celsius to Fahrenheit ---")
print("Temperatura en °C | Temperatura en °F")
print("-" * 35)

for celsius in range(0, 101, 10):  # De 0 a 100 en pasos de 10
    fahrenheit = (celsius * 9/5) + 32
    print(f"{celsius:>15}°C | {fahrenheit:>15.1f}°F")

# Ejercicio 3: Detección de valores críticos
print("\n--- Ejercicio 3: Valores críticos en experimento ---")
valores_experimento = [12.5, 8.3, 15.7, 22.1, 9.8, 18.4, 25.0, 7.2]

print(f"Valores del experimento: {valores_experimento}")
print("Análisis de valores:")

for valor in valores_experimento:
    if valor > 20.0:
        print(f"  {valor} → ¡VALOR CRÍTICO! (mayor que 20.0)")
    elif valor < 10.0:
        print(f"  {valor} → Valor bajo (menor que 10.0)")
    else:
        print(f"  {valor} → Valor normal")

# =============================================================================
# 5. CONTROLADORES ADICIONALES: break, continue, pass
# =============================================================================
print("\n" + "="*60)
print("5. CONTROLADORES ADICIONALES: break, continue, pass")
print("="*60)

# Ejemplo de break: Detener cuando se encuentra un valor
print("\n--- 5.1 Uso de break ---")
print("Buscando el primer valor mayor que 15:")
for valor in valores_experimento:
    print(f"  Probando valor: {valor}")
    if valor > 15.0:
        print(f"  ¡Encontrado! {valor} > 15.0")
        break

# Ejemplo de continue: Saltar valores específicos
print("\n--- 5.2 Uso de continue ---")
print("Procesando valores (saltando los < 10):")
for valor in valores_experimento:
    if valor < 10.0:
        continue  # Saltar este valor
    print(f"  Procesando valor: {valor}")

# Ejemplo de pass: Marcador de posición
print("\n--- 5.3 Uso de pass ---")
for valor in valores_experimento:
    if valor > 20.0:
        pass  # Aquí iría código para manejar valores críticos
        # Por ahora solo es un marcador
    else:
        print(f"  Valor normal: {valor}")

# =============================================================================
# EJECUCIÓN PRINCIPAL
# =============================================================================
if __name__ == "__main__":
    print("\n" + "="*60)
    print("¡CLASE DE CONTROL DE FLUJO COMPLETADA!")
    print("="*60)
    print("\nResumen de temas cubiertos:")
    temas = [
        "1. Estructuras condicionales (if, elif, else)",
        "2. Bucle while con aplicaciones físicas", 
        "3. Bucle for con range() y tuplas",
        "4. Ejercicios prácticos de física computacional",
        "5. Controladores adicionales (break, continue, pass)"
    ]
    for i, tema in enumerate(temas, 1):
        print(f"  {i}. {tema}")
    
    print("\n" + "="*60)
    print("¡Próxima clase: Funciones y manejo de excepciones!")
    print("="*60)
