import sys
##import math
##import matplotlib.pyplot as plt

EPSILON = sys.float_info.epsilon

def biseccion(f, a, b, max_iter=1000, TOL=EPSILON):
    history = []
    try:
        if f(a) * f(b) > 0:
            raise ValueError("No se puede asegurar que la función tenga una raíz en [a,b]")

        if f(a) == 0:
            return a, 0, [a]
        if f(b) == 0:
            return b, 0, [b]

        counter = 0
        while abs(b - a) > TOL and counter < max_iter:
            m = a + 0.5 * (b - a)
            history.append(m)
            if f(a) * f(m) < 0:
                b = m
            else:
                a = m
            counter += 1

        return m, counter, history

    except Exception as e:
        print(f"[Error en Bisección] {e}")
        return None, 0, []


def newton(f, df, x0, max_iter=1000, TOL=EPSILON):
    """
    Newton con criterio relativo escalado usando EPSILON como base.
    Devuelve última aproximación + historial aunque no converja.
    """
    history = []
    x = x0
    try:
        for i in range(max_iter):
            fx = f(x)
            dfx = df(x)
            if dfx == 0:
                raise ZeroDivisionError("Derivada nula: no se puede continuar")

            x_new = x - fx / dfx
            history.append(x_new)

            # criterio relativo escalado (usa EPSILON)
            if abs(x_new - x) < TOL * max(1.0, abs(x_new)):
                return x_new, i + 1, history

            x = x_new

        # no convergió: devolvemos la última aproximación y el número de iteraciones
        print("Warning: Newton-Raphson no llegó a EPSILON; devolviendo última aproximación.")
        return x, max_iter, history

    except Exception as e:
        print(f"[Error en Newton-Raphson] {e}")
        return None, 0, []
    

def secante(f, x0, x1, max_iter=1000, TOL=EPSILON):
    """
    Secante con criterio relativo escalado.
    Devuelve última aproximación + historial aunque no converja.
    """
    history = []
    try:
        for i in range(max_iter):
            f0, f1 = f(x0), f(x1)
            denom = (f1 - f0)
            if denom == 0:
                raise ZeroDivisionError("Diferencia nula: no se puede continuar")

            x2 = x1 - f1 * (x1 - x0) / denom
            history.append(x2)

            if abs(x2 - x1) < TOL * max(1.0, abs(x2)):
                return x2, i + 1, history

            x0, x1 = x1, x2

        print("Warning: Secante no llegó a EPSILON; devolviendo última aproximación.")
        return x1, max_iter, history

    except Exception as e:
        print(f"[Error en Secante] {e}")
        return None, 0, []


if __name__ == "__main__":
    f = lambda x: x**2 - 2
    df = lambda x: 2*x

    print("\n=== Método de Bisección ===")
    raiz_biseccion, it_b, hist_b = biseccion(f, 0, 2)
    print(f"Raíz aproximada: {raiz_biseccion}, Iteraciones: {it_b}")

    print("\n=== Método de Newton-Raphson ===")
    raiz_newton, it_n, hist_n = newton(f, df, 1.0)
    print(f"Raíz aproximada: {raiz_newton}, Iteraciones: {it_n}")

    print("\n=== Método de la Secante ===")
    raiz_secante, it_s, hist_s = secante(f, 1.0, 2.0)
    print(f"Raíz aproximada: {raiz_secante}, Iteraciones: {it_s}")

    # Gráfica (siempre usando las trayectorias disponibles)
###    raiz_real = math.sqrt(2)
###    plt.figure(figsize=(8,5))
###    if hist_b:
###        plt.semilogy(range(1, len(hist_b)+1), [abs(x - raiz_real) for x in hist_b], label="Bisección", marker="o")
###    if hist_n:
###        plt.semilogy(range(1, len(hist_n)+1), [abs(x - raiz_real) for x in hist_n], label="Newton-Raphson", marker="s")
###    if hist_s:
###        plt.semilogy(range(1, len(hist_s)+1), [abs(x - raiz_real) for x in hist_s], label="Secante", marker="^")
###
###    plt.xlabel("Iteraciones")
###    plt.ylabel("Error absoluto (escala log)")
###    plt.title("Desempeño de los métodos numéricos (criterio relativo con EPSILON)")
###    plt.legend()
###    plt.grid(True, which="both", ls="--")
###    plt.show()
###
