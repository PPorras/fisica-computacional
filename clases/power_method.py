#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
power_method.py
---------------

Calcula los valores propios dominantes de una matriz usando:
- Método de la potencia.
- Deflación para el segundo valor propio.

Usa funciones auxiliares de `power_utils.py`.
"""

from matrix import Matrix
from power_utils import normalize, matrix_vector_product, outer_product


# ======================
# Método de la potencia
# ======================
def power_method(A, tol=1e-10, max_iter=1000, verbose=True):
    """
    Calcula el valor propio dominante mediante el método de la potencia.
    """
    if A.rows != A.cols:
        raise ValueError("La matriz debe ser cuadrada.")

    v = [1.0 for _ in range(A.cols)]
    lambda_old = 0.0

    for it in range(max_iter):
        Av = matrix_vector_product(A, v)
        v_new = normalize(Av)
        lambda_new = sum(v_new[i] * Av[i] for i in range(A.cols))

        if abs(lambda_new - lambda_old) < tol:
            if verbose:
                print(f"Convergió en {it+1} iteraciones.")
            return lambda_new, v_new

        v = v_new
        lambda_old = lambda_new

        if verbose and it % 10 == 0:
            print(f"Iter {it:4d}: lambda approx {lambda_new:.10f}")

    raise RuntimeError("El método de la potencia no convergió.")


# ======================
# Método de deflación
# ======================
def deflation(A, lambda1, v1):
    """
    Aplica deflación a la matriz A para eliminar la contribución
    del valor propio dominante (lambda1, v1).

    A' = A - lambda_1 * v_1 * v1T
    """
    v1 = normalize(v1)
    outer = outer_product(v1, v1)
    scaled = outer * lambda1
    return A - scaled


# ======================
# Ejemplo de uso
# ======================
if __name__ == "__main__":
    A = Matrix([[4, 1, -2],
                [1, 2, 0],
                [-2, 0, 3]])

    print("Matriz A:")
    print(A)

    print("\n=== Primer valor propio (dominante) ===")
    lambda1, v1 = power_method(A, tol=1e-8)
    print(f"lambda_1 approx {lambda1:.10f}")
    print(f"v_1 approx {v1}")

    print("\n=== Aplicando deflación ===")
    A_def = deflation(A, lambda1, v1)

    print("Matriz A' (deflactada):")
    print(A_def)

    print("\n=== Segundo valor propio ===")
    lambda2, v2 = power_method(A_def, tol=1e-8)
    print(f"lambda_2 approx {lambda2:.10f}")
    print(f"V_2 approx {v2}")

