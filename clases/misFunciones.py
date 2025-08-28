def isPrime(number: int) -> bool:
    """
    Verifica si un número es primo.

    Args:
        number (int): Número a verificar.
        
    Returns:
        bool: True si es primo, False si no lo es.

    Raises:
        TypeError: Si la entrada no es un entero.
    """
    try:
        # Verificar tipo
        if not isinstance(number, int):
            raise TypeError(f"Se esperaba un int, pero se recibió {type(number).__name__}")

        if number <= 1:
            return False
        elif number == 2:
            return True
        elif number % 2 == 0:
            return False

        # Verificar divisibilidad por números impares
        for i in range(3, int(number**0.5) + 1, 2):
            if number % i == 0:
                return False
        return True

    except TypeError as e:
        print("Error de tipo:", e)
        return False
    finally:
        print(f"Se intentó verificar si {number} es primo.")


def myFactorial(number: int) -> int:
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
        #    - x debe ser float o int
        #    - tol debe ser None o float positivo
        #    - raise TypeError o ValueError si no cumplen

        # 2. Si tol es None, asignar epsilon de maquina

        # 3. Manejar el caso x < 0
        #    - usar la relación e^x = 1 / e^(-x)

        # 4. Manejar el caso x == 0
        #    - devolver 1.0

        # 5. Inicializar variables para la serie:
        #    resultado = 1.0
        #    termino = 1.0
        #    n = 1

        # 6. Bucle:
        #    - calcular el siguiente término de la serie
        #    - sumar al resultado
        #    - criterio de parada: abs(termino) < tol * abs(nuevo_resultado)

        # 7. Devolver resultado final

        pass  #

    except (TypeError, ValueError) as e:
        print("Error en exponencial_taylor:", e)
        return None
    finally:
        print(f"Se intentó calcular e^{x} con tolerancia {tol}.")


if __name__ == "__main__":
    # Pruebas de isPrime
    print("\nPruebas de isPrime:")
    print("¿2 es primo?", isPrime(2))
    print("¿15 es primo?", isPrime(15))
    print("¿'a' es primo?", isPrime("a"))

    # Pruebas de myFactorial
    print("\nPruebas de myFactorial:")
    print("5! =", myFactorial(5))
    print("(-3)! =", myFactorial(-3))
    print("'x'! =", myFactorial("x"))

    # Pruebas de la función
    print("\nPruebas de exponencial_taylor:")
    print("e^0 =", exponencial_taylor(0))
    print("e^1 =", exponencial_taylor(1))
    print("e^-2 =", exponencial_taylor(-2))
    print("Con tolerancia inválida:", exponencial_taylor(1, tol=-0.1))
    print("Con tipo inválido:", exponencial_taylor("a"))
