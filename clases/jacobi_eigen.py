"""
jacobi_eigen.py
----------------
Implementación del método de Jacobi para calcular autovalores y autovectores
de una matriz simétrica real A ∈ R^{n×n}.

Requiere:
    from matrix import Matrix
Autor: [Tu nombre]
Curso: Física Computacional / Álgebra Lineal Numérica
"""

from matrix import Matrix
from math import sqrt, copysign

def jacobi_eigen(A: Matrix, tol=1e-10, max_iter=100):
    """
    Método de Jacobi para diagonalizar una matriz simétrica.

    Parameters
    ----------
    A : Matrix
        Matriz simétrica real.
    tol : float
        Tolerancia para los elementos fuera de la diagonal.
    max_iter : int
        Número máximo de iteraciones.

    Returns
    -------
    D : Matrix
        Matriz diagonal con los autovalores.
    Q : Matrix
        Matriz ortogonal con los autovectores en columnas.
    """

    n = A.rows
    if n != A.cols:
        raise ValueError("La matriz debe ser cuadrada.")

    # Copiamos A para no modificarla directamente
    A = A.copy()
    Q = Matrix([[1.0 if i == j else 0.0 for j in range(n)] for i in range(n)])

    for it in range(max_iter):

        # Paso 2: buscar el elemento fuera de la diagonal más grande en valor absoluto
        p, q = 0, 1
        max_val = abs(A.data[p][q])
        for i in range(n):
            for j in range(i + 1, n):
                if abs(A.data[i][j]) > max_val:
                    p, q = i, j
                    max_val = abs(A.data[i][j])

        # Condición de parada
        if max_val < tol:
            break

        # Paso 3: calcular el ángulo de rotación
        if A.data[p][p] == A.data[q][q]:
            theta = 3.141592653589793 / 4  # pi/4
        else:
            tau = (A.data[q][q] - A.data[p][p]) / (2 * A.data[p][q])
            t = copysign(1.0 / (abs(tau) + sqrt(1 + tau**2)), tau)
            c = 1 / sqrt(1 + t**2)
            s = t * c

        # Paso 4: construir J(p,q) e implementar la rotación
        for i in range(n):
            if i != p and i != q:
                aip = A.data[i][p]
                aiq = A.data[i][q]
                A.data[i][p] = c * aip - s * aiq
                A.data[p][i] = A.data[i][p]  # mantener simetría
                A.data[i][q] = c * aiq + s * aip
                A.data[q][i] = A.data[i][q]

        app = A.data[p][p]
        aqq = A.data[q][q]
        apq = A.data[p][q]

        A.data[p][p] = c**2 * app - 2 * s * c * apq + s**2 * aqq
        A.data[q][q] = s**2 * app + 2 * s * c * apq + c**2 * aqq
        A.data[p][q] = 0.0
        A.data[q][p] = 0.0

        # Actualizar matriz de autovectores Q = QJ
        for i in range(n):
            qip = Q.data[i][p]
            qiq = Q.data[i][q]
            Q.data[i][p] = c * qip - s * qiq
            Q.data[i][q] = s * qip + c * qiq

    return A, Q


# =====================================================
# Ejemplo de uso
# =====================================================
if __name__ == "__main__":
    A = Matrix([[4, -2, 2],
                [-2, 1, 0],
                [2, 0, 3]])

    print("Matriz A:")
    print(A)
    print("\n--- Método de Jacobi ---")
    D, Q = jacobi_eigen(A, tol=1e-10)
    print("\nMatriz diagonal D (autovalores):")
    print(D)
    print("\nMatriz Q (autovectores):")
    print(Q)

