"""
Demo de cancelación catastrófica en el cálculo de cos(x) usando series de Taylor.
"""

from misFunciones import coseno_taylor, epsilon_maquina, mi_factorial
import matplotlib.pyplot as plt

def demostrar_cancelacion_catastrofica():
    """
    Demuestra el fenómeno de cancelación catastrófica en el cálculo del coseno.
    """
    print("=" * 70)
    print("DEMOSTRACIÓN DE CANCELACIÓN CATASTRÓFICA")
    print("=" * 70)
    
    # Valores de x donde ocurre cancelación catastrófica
    valores_x = [10.0, 20.0, 30.0, 40.0, 50.0, 100.0, 150.0, 200.0]
    
    print(f"{'x':>8} {'Nuestro cos(x)':>20} {'math.cos(x)':>20} {'Error absoluto':>20} {'Error relativo':>20}")
    print("-" * 90)
    
    errores = []
    
    for x in valores_x:
        try:
            # Nuestro cálculo
            nuestro_cos = coseno_taylor(x, epsilon_maquina())
            
            print(f"{x:8.1f} {nuestro_cos:20.10f} {math_cos:20.10f} {error_absoluto:20.2e} {error_relativo:20.2e}")
            
        except Exception as e:
            print(f"{x:8.1f} ERROR: {e}")
            errores.append(float('nan'))
    
    return valores_x, errores

def analizar_terminos_serie(x: float):
    """
    Analiza los términos individuales de la serie de Taylor para cos(x).
    """
    print(f"\n\nANÁLISIS DE TÉRMINOS PARA cos({x}):")
    print("=" * 60)
    print(f"{'n':>4} {'|Término|':>15} {'Suma acumulada':>20} {'Contribución':>15}")
    print("-" * 60)
    
    suma = 0.0
    terminos = []
    sumas_acumuladas = []
    
    for n in range(100):  # Analizamos los primeros 100 términos
        signo = 1 if n % 2 == 0 else -1
        exponente = 2 * n
        termino = signo * (x ** exponente) / i_factorial(exponente)
        
        suma_anterior = suma
        suma += termino
        terminos.append(abs(termino))
        sumas_acumuladas.append(suma)
        
        # Solo mostrar términos significativos
        if abs(termino) > 1e-100:
            contribucion = abs(termino) / abs(suma) if suma != 0 else float('inf')
            print(f"{n:4} {abs(termino):15.2e} {suma:20.10f} {contribucion:15.2e}")
        
        # Detener cuando los términos sean insignificantes
        if abs(termino) < 1e-300:
            break
    
    return terminos, sumas_acumuladas

def graficar_comportamiento():
    """
    Grafica el error relativo en función de x.
    """
    print("\n\nGRÁFICO DE COMPORTAMIENTO:")
    print("=" * 50)
    
    # Generar valores de x
    x_values = np.linspace(0, 200, 100)
    errores_relativos = []
    
    for x in x_values:
        try:
            nuestro = coseno_taylor(x, 1e-12)
            math_val = math.cos(x)
            error = abs(nuestro - math_val) / abs(math_val) if math_val != 0 else float('inf')
            errores_relativos.append(error)
        except:
            errores_relativos.append(float('nan'))
    
    # Crear gráfico
    plt.figure(figsize=(12, 8))
    
    plt.subplot(2, 1, 1)
    plt.plot(x_values, errores_relativos, 'b-', linewidth=2)
    plt.yscale('log')
    plt.xlabel('x')
    plt.ylabel('Error relativo')
    plt.title('Error relativo de coseno_taylor vs math.cos')
    plt.grid(True, alpha=0.3)
    
    plt.subplot(2, 1, 2)
    plt.plot(x_values, np.cos(x_values), 'r-', linewidth=2)
    plt.xlabel('x')
    plt.ylabel('cos(x)')
    plt.title('Función cos(x) real')
    plt.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.savefig('cancelacion_catastrofica.png', dpi=300, bbox_inches='tight')
    plt.show()

def comparar_con_reduccion():
    """
    Compara nuestro método con y sin reducción de rango (simulada).
    """
    print("\n\nCOMPARACIÓN CON REDUCCIÓN DE RANGO:")
    print("=" * 60)
    
    # Valores problemáticos
    valores_problematicos = [50.0, 100.0, 150.0, 200.0]
    
    print(f"{'x':>8} {'Sin reducción':>20} {'Con reducción':>20} {'math.cos':>20}")
    print("-" * 78)
    
    for x in valores_problematicos:
        # Sin reducción (nuestro método actual)
        sin_reduccion = coseno_taylor(x, 1e-12)
        
        # Con reducción (usando propiedad de periodicidad)
        x_reducido = x % (2 * math.pi)  # Reducir al rango [0, 2π)
        con_reduccion = coseno_taylor(x_reducido, 1e-12)
        
        math_val = math.cos(x)
        
        error_sin = abs(sin_reduccion - math_val) if sin_reduccion is not None else float('inf')
        error_con = abs(con_reduccion - math_val) if con_reduccion is not None else float('inf')
        
        print(f"{x:8.1f} {error_sin:20.2e} {error_con:20.2e} {math_val:20.10f}")

def ejemplo_cancelacion_extrema():
    """
    Muestra un ejemplo extremo de cancelación catastrófica.
    """
    print("\n\nEJEMPLO EXTREMO DE CANCELACIÓN CATASTRÓFICA:")
    print("=" * 60)
    
    x = 1000.0
    print(f"Calculando cos({x})...")
    
    try:
        # Intentar calcular directamente
        resultado_directo = coseno_taylor(x, 1e-12)
        math_val = math.cos(x)
        
        print(f"Resultado directo: {resultado_directo}")
        print(f"math.cos:         {math_val}")
        print(f"Error absoluto:   {abs(resultado_directo - math_val):.2e}")
        print(f"Error relativo:   {abs(resultado_directo - math_val)/abs(math_val):.2e}")
        
        # Demostrar por qué ocurre la cancelación
        print(f"\n¿Por qué ocurre la cancelación?")
        print(f"x^2 = {x**2:.2e}")
        print(f"Términos de la serie crecen hasta ~x^{2*50} = {x**(100):.2e}")
        print(f"Pero 100! = {i_factorial(100):.2e}")
        print("¡Los términos individuales son enormes pero se cancelan!")
        
    except Exception as e:
        print(f"Error: {e}")

def main():
    """
    Función principal que ejecuta todas las demostraciones.
    """
    print("MAIN.PY - Demostración de Cancelación Catastrófica")
    print("=" * 60)
    
    # 1. Demostración principal
    valores_x, errores = demostrar_cancelacion_catastrofica()
    
    # 2. Análisis detallado para un valor específico
    x_analisis = 30.0
    terminos, sumas = analizar_terminos_serie(x_analisis)
    
    # 3. Comparación con reducción de rango
    comparar_con_reduccion()
    
    # 4. Ejemplo extremo
    ejemplo_cancelacion_extrema()
    
    # 5. Mostrar gráfico (opcional - descomentar si quieres ver el gráfico)
    # graficar_comportamiento()
    
    print("\n" + "=" * 60)
    print("CONCLUSIÓN:")
    print("La cancelación catastrófica ocurre cuando:")
    print("1. Los términos individuales de la serie son muy grandes")
    print("2. Pero su suma es relativamente pequeña")
    print("3. Los errores de redondeo en términos grandes 'contaminan' el resultado")
    print("4. La precisión se pierde debido a la resta de números casi iguales")

if __name__ == "__main__":
    main()
