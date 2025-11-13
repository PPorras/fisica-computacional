def mi_factorial(number: int) -> int:
    """
    Calcula el factorial de un número no negativo.

    Args:
        number (int): Número al calcular el factorial.
        
    Returns:
        int: El factorial del número.

    Raises:
        TypeError: Si la entrada no es un entero.
        ValueError: Si la entrada es negativa.
    """
    try:
        # Verificar tipo
        if not isinstance(number, int):
            raise TypeError(f"Se esperaba un int, pero se recibió {type(number).__name__}")

        if number < 0:
            raise ValueError("Se espera un int mayor o igual que cero")

        # Cálculo del factorial
        result = 1
        for i in range(1, number + 1):
            result *= i
        return result

    except (TypeError, ValueError) as e:
        print("Error en factorial:", e)
        return None
    finally:
        print(f"Se intentó calcular el factorial de {number}.")


def epsilon_maquina():
        """
        Calcula el épsilon usando el método básico de división sucesiva.

        Returns:
            float: El valor del épsilon de máquina
        """

        epsilon = 1.0
        while True:
            ##epsilon_mach = epsilon 
            epsilon = 0.5*epsilon
            if 1.0 + epsilon == 1.0:
                break
        # COMPLETAR AQUÍ
        return 2.0*epsilon

def calcular_underflow():
        """
        Calcula el épsilon usando el método básico de división sucesiva.

        Returns:
            float: El valor del épsilon de máquina
        """

        epsilon = 1.0
        while True:
            under_flow = epsilon ## epsilon = 0.5*epsilon
            epsilon *= 0.5 ## epsilon = 0.5*epsilon
            if epsilon == 0.0:
                break
        # COMPLETAR AQUÍ
        return under_flow

def calcular_overflow():
        """
        Calcula el épsilon usando el método básico de división sucesiva.

        Returns:
            float: El valor del épsilon de máquina
        """

        epsilon = 1.0
        while True:
            over_flow = epsilon ## epsilon = 0.5*epsilon
            epsilon *= 2.0 ## epsilon = 0.5*epsilon
            if epsilon == float('inf'):
                break
        # COMPLETAR AQUÍ
        return over_flow

def exponencial_taylor(x: float, tol: float = None) -> float:
    """
    Calcula e^x usando la serie de Taylor con una tolerancia dada.

    Args:
        x (float): Valor para calcular e^x.
        tol (float, opcional): Tolerancia. Por defecto usa épsilon de máquina.

    Returns:
        float: Aproximación de e^x.

    Raises:
        TypeError: Si x o tol no son del tipo numérico esperado.
        ValueError: Si se da una tolerancia no positiva.
    """
    try:
        # 1. Verificar tipo de x y tol
        if not isinstance(x, float):
            raise TypeError(f"x debe ser numérico, se recibió: {type(x).__name__}")
        
        if tol is not None and not isinstance(tol, float):
            raise TypeError(f"tol debe ser numérico o None, se recibió: {type(tol).__name__}")
        
        # 2. Si tol es None, asignar epsilon de maquina
        if tol is None:
            ###tol = sys.float_info.epsilon
            tol = epsilon_maquina()
        elif tol <= 0:
            raise ValueError(f"tol debe ser positiva, se recibió: {tol}")
        
        # 3. Manejar el caso x < 0
        if x < 0:
            return 1.0 / exponencial_taylor(-x, tol)
        
        # 4. Manejar el caso x == 0
        if x == 0:
            return 1.0
        
        # 5. Inicializar variables para la serie:
        resultado = 1.0
        termino = 1.0
        n = 1
        
        # 6. Bucle de la serie de Taylor:
        while True:
            # Calcular el siguiente término de la serie
            termino *= x / n
            nuevo_resultado = resultado + termino
            
            # Verificar posibles problemas numéricos
            #if math.isinf(nuevo_resultado):
            #    raise OverflowError(f"Overflow al calcular e^{x}")
            
            # Criterio de parada: el término es insignificante comparado con el resultado
            if abs(termino) < tol * abs(nuevo_resultado):
                resultado = nuevo_resultado
                break
            
            resultado = nuevo_resultado
            n += 1
            
            # Prevención de bucle infinito (aunque debería converger)
            if n > 1000:
                raise RuntimeError(f"No se alcanzó convergencia en {n} iteraciones")
        
        # 7. Devolver resultado final
        return resultado

    except (TypeError, ValueError, OverflowError, RuntimeError) as e:
        print("Error en exponencial_taylor:", e)
        return None
    finally:
        print(f"Se intentó calcular e^{x} con tolerancia {tol}.")

def mi_raiz_cuadrada(x: float, tol: float = None) -> float:
    """
    Calcula la raíz cuadrada de un número positivo usando el método de Newton-Raphson.

    Args:
        x (float): Número del que se quiere calcular la raíz cuadrada.
        tol (float, opcional): Tolerancia de convergencia. Si no se da, se usa el épsilon de máquina.

    Returns:
        float: Aproximación de sqrt(x).

    Raises:
        TypeError: Si x o tol no son del tipo correcto.
        ValueError: Si x es negativo.
        RuntimeError: Si no converge.
    """
    try:
        if not isinstance(x, (int, float)):
            raise TypeError(f"x debe ser numérico, se recibió: {type(x).__name__}")
        if x < 0:
            raise ValueError("No se puede calcular la raíz cuadrada de un número negativo.")
        if tol is not None and not isinstance(tol, float):
            raise TypeError(f"tol debe ser numérico o None, se recibió: {type(tol).__name__}")
        if tol is None:
            tol = epsilon_maquina()

        # Casos triviales
        if x == 0:
            return 0.0
        if x == 1:
            return 1.0

        # Método de Newton-Raphson
        y = x / 2.0
        for _ in range(1000):
            y_new = 0.5 * (y + x / y)
            if abs(y_new - y) < tol * abs(y_new):
                return y_new
            y = y_new

        raise RuntimeError("No se alcanzó convergencia en 1000 iteraciones.")

    except (TypeError, ValueError, RuntimeError) as e:
        ###print("Error en mi_raiz_cuadrada:", e)
        return None
    ##finally:
        ###print(f"Se intentó calcular sqrt({x}) con tolerancia {tol}.")

def mi_seno(x: float, tol: float = None) -> float:
    """
    Calcula sin(x) usando la serie de Taylor en 0:
        sin(x) = x - x^3/3! + x^5/5! - x^7/7! + ...

    Args:
        x (float): Valor en radianes.
        tol (float, opcional): Tolerancia relativa para el criterio de parada.
                               Si no se especifica, se usa el épsilon de máquina.

    Returns:
        float: Aproximación de sin(x).

    Raises:
        TypeError: Si x o tol no son del tipo esperado.
        ValueError: Si tol no es positiva.
        RuntimeError: Si no converge en el número máximo de iteraciones.
    """
    original_x = x
    try:
        # Verificaciones de tipo
        if not isinstance(x, (int, float)):
            raise TypeError(f"x debe ser numérico, se recibió: {type(x).__name__}")
        if tol is not None and not isinstance(tol, float):
            raise TypeError(f"tol debe ser numérico o None, se recibió: {type(tol).__name__}")

        # Si tol es None, usamos el épsilon de máquina
        if tol is None:
            tol = epsilon_maquina()
        elif tol <= 0:
            raise ValueError(f"tol debe ser positiva, se recibió: {tol}")

        # Convertir x a float explícitamente
        x = float(x)

        # Caso trivial
        if x == 0.0:
            return 0.0

        # Serie de Taylor: sin(x) = Σ (-1)^n * x^(2n+1) / (2n+1)!
        # Calculamos usando recurrencia:
        resultado = x         # primer término: x^1 / 1!
        termino = x
        n = 1
        max_iter = 1000

        while True:
            # Recurrencia del término:
            # t_{n+1} = t_n * ( -x^2 / ((2n)*(2n+1)) )
            termino *= - (x * x) / ((2 * n) * (2 * n + 1))
            nuevo_resultado = resultado + termino

            # Criterio de parada relativo
            if abs(termino) < tol * abs(nuevo_resultado):
                resultado = nuevo_resultado
                break

            resultado = nuevo_resultado
            n += 1

            if n > max_iter:
                raise RuntimeError(f"No se alcanzó convergencia en {max_iter} iteraciones.")

        return resultado

    except (TypeError, ValueError, RuntimeError) as e:
        ###print("Error en mi_seno:", e)
        return None
    ##finally:
        ###print(f"Se intentó calcular sin({original_x}) con tolerancia {tol}.")



if __name__ == "__main__":
    # Pruebas de isPrime

    ###### Pruebas de la función
    print("\nPruebas de exponencial_taylor:")
    print("e^0 =", exponencial_taylor(0.0))
    print("e^1 =", exponencial_taylor(1.0))
    print("e^-2 =", exponencial_taylor(-2.0))
    print("Con tolerancia inválida:", exponencial_taylor(1, tol=-0.1))
    print("Con tipo inválido:", exponencial_taylor("a"))

    print(f'\n El epsilon de maquina es {epsilon_maquina()}')
    print(f'\n El epsilon de maquina entre dos más uno es {1.0 +  0.5*epsilon_maquina()}')
    print(f'\n El Underflow es  {calcular_underflow()}')
    print(f'\n Comprobamos que si es el  underflow es  {0.5*calcular_underflow()}')
    print(f'\n Overflow es  {calcular_overflow()}')
    print(f'\n Comprobamos que si es el  underflow es  {2.0*calcular_overflow()}')

    print("\nPruebas de mi_raiz_cuadrada:")
    print("sqrt(4) =", mi_raiz_cuadrada(4.0))
    print("sqrt(2) approx", mi_raiz_cuadrada(2.0))
    print("sqrt(0) =", mi_raiz_cuadrada(0.0))
    print("Entrada inválida:", mi_raiz_cuadrada(-9.0))

