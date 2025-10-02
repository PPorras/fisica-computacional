#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
least_squares_demo.py
---------------------

Script de demostración de Mínimos Cuadrados para la clase.

Ejemplos:
- Ecuaciones normales
- Sistema aumentado
- Factorización QR (Gram-Schmidt)

Usa matrix.py y linear_systems.py
"""

from matrix import Matrix
from linear_systems import gaussian_elimination, lu_solve

def generate_data():
    """
    Genera datos simples: y ≈ 2x + 1 con ruido.
    """
    x = [0, 1, 2, 3, 4, 5]
    y = [1.0, 2.9, 5.1, 6.2, 9.1, 10.2]
    # Matriz A para ajuste lineal: y ≈ a + b*x
    A = Matrix([[1, xi] for xi in x])
    b = [yi for yi in y]
    return A, b

def normal_equations(A: Matrix, b: list):
    """
    Resuelve el problema de mínimos cuadrados usando ecuaciones normales:
        (A^T A)x = A^T b
    """
    At = A.transpose()
    AtA = At * A
    Atb = [sum(At.data[i][k] * b[k] for k in range(A.rows)) for i in range(A.cols)]
    return gaussian_elimination(AtA, Atb)

def augmented_system(A: Matrix, b: list):
    """
    Resuelve mínimos cuadrados mediante sistema aumentado:
        [ I   A ] [r]   [b]
        [A^T 0 ] [x] = [0]
    """
    m, n = A.shape()

    # Bloque superior: [I  A]
    top = [([1 if i==j else 0 for j in range(m)] + A.data[i]) for i in range(m)]

    # Bloque inferior: [A^T  0]
    At = A.transpose()
    bottom = [At.data[i] + [0]*n for i in range(n)]

    # Ensamblamos matriz aumentada
    augM = top + bottom
    rhs = b + [0]*n

    sol = gaussian_elimination(Matrix(augM), rhs)

    return sol[m:]  # devolvemos solo x

def qr_factorization(A: Matrix, b: list):
    """
    Gram-Schmidt clásico para obtener Q y R,
    luego resolver Rx = Q^T b
    """
    m, n = A.shape()
    # Copia columnas de A
    Qcols = []
    R = [[0]*n for _ in range(n)]

    for j in range(n):
        v = [row[j] for row in A.data]
        for k in range(j):
            qk = [row[k] for row in Qcols]
            R[k][j] = sum(qk[i]*v[i] for i in range(m))
            v = [v[i] - R[k][j]*qk[i] for i in range(m)]
        norm = sum(vi**2 for vi in v) ** 0.5
        R[j][j] = norm
        qj = [vi / norm for vi in v]
        for i in range(m):
            if j == 0:
                Qcols.append([qj[i]])
            else:
                Qcols[i].append(qj[i])

    Q = Matrix(Qcols)
    R = Matrix(R)

    # Resolver Rx = Q^T b
    Qtb = [sum(Q.data[i][j] * b[i] for i in range(m)) for j in range(n)]
    return gaussian_elimination(R, Qtb)

def main():
    A, b = generate_data()

    print("Matriz A:")
    print(A)
    print("Vector b:", b)

    # Método 1: Ecuaciones normales
    x_ne = normal_equations(A, b)
    print("\n--- Normal Equations ---")
    print("Coeficientes:", x_ne)

    # Método 2: Sistema aumentado
    x_aug = augmented_system(A, b)
    print("\n--- Augmented System ---")
    print("Coeficientes:", x_aug)

    # Método 3: Factorización QR
    x_qr = qr_factorization(A, b)
    print("\n--- QR (Gram-Schmidt) ---")
    print("Coeficientes:", x_qr)


if __name__ == "__main__":
    main()

