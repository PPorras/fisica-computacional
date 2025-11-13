import numpy as np
import math

def ejemplo_cancelacion_basica():
    """Ejemplo cancelación catastrófica"""
    print("=== EJEMPLO BÁSICO  ===")
    
    # Números MUY cercanos para forzar cancelación
    x = 1.000000000000001
    y = 1.000000000000000
    
    # Diferencia real (exacta)
    diferencia_real = 0.000000000000001
    
    # Diferencia calculada (con error de punto flotante)
    diferencia_calculada = x - y
    
    print(f"x = {x:.20f}")
    print(f"y = {y:.20f}")
    print(f"Diferencia real:    {diferencia_real:.20f}")
    print(f"Diferencia calculada: {diferencia_calculada:.20f}")
    print(f"Error relativo: {abs((diferencia_calculada - diferencia_real) / diferencia_real):.2e}")
    print(f"¡El error es del {abs((diferencia_calculada - diferencia_real) / diferencia_real)*100:.1f}%!")

def ejemplo_raiz_cuadratica():
    """Ejemplode fórmula cuadrática"""
    print("\n=== FÓRMULA CUADRÁTICA CORREGIDA ===")
    
    # Ecuación: x^2 - 1000000.000001x + 1 = 0 (más extrema)
    # Soluciones: x1 approx 1000000, x2 aprox 0.000001
    a, b, c = 1.0, -1000000.000001, 1.0
    
    # Fórmula estándar (SUFRE cancelación catastrófica en x2)
    discriminante = math.sqrt(b**2 - 4*a*c)
    x1_estandar = (-b + discriminante) / (2*a)
    x2_estandar = (-b - discriminante) / (2*a)
    
    # Fórmula mejorada (evita cancelación)
    if b >= 0:
        x1_mejorada = (-b - discriminante) / (2*a)
        x2_mejorada = (2*c) / (-b - discriminante)
    else:
        x1_mejorada = (2*c) / (-b + discriminante)
        x2_mejorada = (-b + discriminante) / (2*a)
    
    print("Ecuación: x^2 - 1000000.000001x + 1 = 0")
    print(f"Solución estándar:  x1 = {x1_estandar:.15f}, x2 = {x2_estandar:.15f}")
    print(f"Solución mejorada:  x1 = {x1_mejorada:.15f}, x2 = {x2_mejorada:.15f}")
    print(f"Valor esperado x2:  0.000001000000000")
    print(f"Error x2 (estándar):  {abs(x2_estandar - 0.000001):.2e}")
    print(f"Error x2 (mejorada): {abs(x2_mejorada - 0.000001):.2e}")
    
    # Verificación: ¿x2 realmente es raíz?
    def es_raiz(x, a, b, c):
        return a*x*x + b*x + c
    
    print(f"\nVerificación:")
    print(f"Ecuación(x2_estandar) = {es_raiz(x2_estandar, a, b, c):.2e}")
    print(f"Ecuación(x2_mejorada) = {es_raiz(x2_mejorada, a, b, c):.2e}")


def demostracion_amplificacion_error():
    """Demuestra cómo se amplifica el error"""
    print("\n=== AMPLIFICACIÓN DEL ERROR ===")
    
    # Error inicial típico en punto flotante
    error_inicial = 1e-16
    
    # Cuando restamos números cercanos, el error se amplifica
    a = 1.0 + error_inicial
    b = 1.0
    
    diferencia = a - b  # Debería ser 1e-16
    
    print(f"a = 1.0 + {error_inicial}")
    print(f"b = 1.0")
    print(f"a - b = {diferencia:.20f}")
    print(f"Error relativo: {abs((diferencia - error_inicial) / error_inicial):.1%}")

# Ejecutar todos los ejemplos CORREGIDOS
if __name__ == "__main__":
    ejemplo_cancelacion_basica()
    ejemplo_raiz_cuadratica()
    demostracion_amplificacion_error()
