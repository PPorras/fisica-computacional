"""
ode_methods.py
--------------

Implementa métodos numéricos para resolver sistemas de ecuaciones
diferenciales ordinarias (EDO) de la forma:

    y' = f(t, y)

Métodos incluidos:
    - Euler explícito
    - Euler implícito (iterativo)
    - Runge–Kutta de cuarto orden (RK4)

"""

from power_utils import vector_add, vector_sub, vector_scale, vector_norm
from numerical_tools import mi_seno as sin


# ===============================================================
# Clase principal
# ===============================================================

class ODESolver:
    def __init__(self, f):
        """
        f : función f(t, y) que devuelve una lista con las derivadas.
        """
        self.f = f

    def euler(self, y0, t0, tf, h, args=()):
        """Método de Euler explícito"""
        t, y = t0, y0[:]
        resultados = [(t, y[:])]
        while t < tf - 1e-12:
            dy = self.f(t, y, *args)
            y = vector_add(y, vector_scale(dy, h))
            t += h
            resultados.append((t, y[:]))
        return resultados

    def euler_implicito(self, y0, t0, tf, h, args=(), tol=1e-8, max_iter=50):
        """Euler implícito mediante iteración de punto fijo"""
        t, y = t0, y0[:]
        resultados = [(t, y[:])]
        while t < tf - 1e-12:
            t_next = t + h
            y_next = y[:]
            for _ in range(max_iter):
                f_eval = self.f(t_next, y_next, *args)
                y_new = vector_add(y, vector_scale(f_eval, h))
                err = vector_norm(vector_sub(y_new, y_next))
                y_next = y_new
                if err < tol:
                    break
            y = y_next
            t = t_next
            resultados.append((t, y[:]))
        return resultados

    def rk4(self, y0, t0, tf, h, args=()):
        """Método de Runge–Kutta de cuarto orden"""
        t, y = t0, y0[:]
        resultados = [(t, y[:])]
        while t < tf - 1e-12:
            k1 = self.f(t, y, *args)
            k2 = self.f(t + h/2, vector_add(y, vector_scale(k1, h/2)), *args)
            k3 = self.f(t + h/2, vector_add(y, vector_scale(k2, h/2)), *args)
            k4 = self.f(t + h, vector_add(y, vector_scale(k3, h)), *args)
            incr = vector_scale(vector_add(k1, vector_add(vector_scale(k2, 2),
                    vector_add(vector_scale(k3, 2), k4))), h/6)
            y = vector_add(y, incr)
            t += h
            resultados.append((t, y[:]))
        return resultados


# ===============================================================
# Ejemplo: péndulo forzado
# ===============================================================

def pendulo_forzado(t, y, q=0.2, F=1.2, Omega=0.7):
    """
    Sistema:
        θ' = ω
        ω' = -sin(θ) - q ω + F sin(Omega t)
    """
    θ, ω = y
    dθ = ω
    dω = -sin(θ) - q * ω + F * sin(Omega * t)
    return [dθ, dω]


if __name__ == "__main__":
    solver = ODESolver(pendulo_forzado)

    y0 = [0.2, 0.0]
    t0, tf, h = 0.0, 10.0, 0.05

    datos_euler = solver.euler(y0, t0, tf, h)
    datos_rk4 = solver.rk4(y0, t0, tf, h)

    print("Método de Euler explícito (primeros pasos):")
    for t, y in datos_euler[:5]:
        print(f"t={t:.2f}, θ={y[0]:.6f}, ω={y[1]:.6f}")

    print("\nMétodo de Runge-Kutta 4 (primeros pasos):")
    for t, y in datos_rk4[:5]:
        print(f"t={t:.2f}, θ={y[0]:.6f}, ω={y[1]:.6f}")

