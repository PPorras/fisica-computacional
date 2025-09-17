"""
Clase de Métodos Numéricos:
Bisección, Newton-Raphson (Tangente) y Secante

Instrucciones:
- Completa dentro de cada método la parte indicada con "TODO".
- Usa EPSILON como criterio de parada.
- Haz que cada método devuelva la raíz aproximada y el número de iteraciones.
"""

import sys

# Epsilon de máquina como tolerancia
EPSILON = sys.float_info.epsilon


def biseccion(f, a, b, max_iter=1000, TOL = EPSILON):
    """
    Método de la Bisección
    """
    try:
        # TODO: Verifica que f(a)*f(b) < 0, si no lanza ValueError
        if  f(a)*f(b) > 0:
            raise ValueError("No se puede asegurar que la funcion tenga una raíz ..")

        if f(a) == 0:
            return a
        elif f(b)==0:
            return b
        else: 
            
            counter = 0
            while abs(b - a) > TOL or counter < max_iter:
                m = a + 0.5*(b-a)

                if f(a)*f(m) < 0:
                    b = m
                else:
                    a = m
                counter += 1

            return m, counter

    except Exception as e:
        print(f"[Error en bisección] {e}")
        return None, 0
    finally:
        print("Bisección finalizó.")


def newton(f, df, x0, max_iter=1000):
    """
    Método de Newton-Raphson (Tangente)
    """
    try:
        x = x0
        for i in range(max_iter):
            # TODO: Calcula fx = f(x) y dfx = df(x)
            # TODO: Revisa si dfx == 0, si sí lanza ZeroDivisionError
            # TODO: Implementa la fórmula de Newton:
            # x_new = ...
            # Criterio de parada: |x_new - x| < EPSILON
            pass

        # TODO: Si no converge en max_iter, lanza RuntimeError

    except Exception as e:
        print(f"[Error en Newton-Raphson] {e}")
        return None, 0
    finally:
        print("Newton-Raphson finalizó.")


def secante(f, x0, x1, max_iter=1000):
    """
    Método de la Secante
    """
    try:
        for i in range(max_iter):
            # TODO: Calcula f0 = f(x0), f1 = f(x1)
            # TODO: Revisa si (f1 - f0) == 0, si sí lanza ZeroDivisionError
            # TODO: Implementa la fórmula de la secante:
            # x2 = ...
            # Criterio de parada: |x2 - x1| < EPSILON
            pass

        # TODO: Si no converge en max_iter, lanza RuntimeError

    except Exception as e:
        print(f"[Error en Secante] {e}")
        return None, 0
    finally:
        print("Secante finalizó.")


if __name__ == "__main__":
    # Ejemplo: encontrar raíz de f(x) = x^2 - 2
    f = lambda x: x**2 - 2
    df = lambda x: 2*x

    print("\n=== Método de Bisección ===")
    raiz_biseccion, it_b = biseccion(f, 0, 2)
    print(f"Raíz aproximada: {raiz_biseccion}, Iteraciones: {it_b}")

    print("\n=== Método de Newton-Raphson ===")
    raiz_newton, it_n = newton(f, df, 1.0)
    print(f"Raíz aproximada: {raiz_newton}, Iteraciones: {it_n}")

    print("\n=== Método de la Secante ===")
    raiz_secante, it_s = secante(f, 1.0, 2.0)
    print(f"Raíz aproximada: {raiz_secante}, Iteraciones: {it_s}")

