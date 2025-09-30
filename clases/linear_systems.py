"""
linear_systems.py
Implementación de métodos para resolver sistemas lineales.
"""

from matrix import Matrix

def forward_substitution(L: Matrix, b: list) -> list:
    """
    Resuelve Ly = b cuando L es triangular inferior.
    """
    n = L.rows
    y = [0] * n
    for i in range(n):
        suma = sum(L.data[i][j] * y[j] for j in range(i))
        y[i] = (b[i] - suma) / L.data[i][i]
    return y


def backward_substitution(U: Matrix, y: list) -> list:
    """
    Resuelve Ux = y cuando U es triangular superior.
    """
    n = U.rows
    x = [0] * n
    for i in reversed(range(n)):
        suma = sum(U.data[i][j] * x[j] for j in range(i + 1, n))
        x[i] = (y[i] - suma) / U.data[i][i]
    return x


def gaussian_elimination(A: Matrix, b: list) -> list:
    """
    Resuelve Ax = b usando eliminación de Gauss sin pivoteo.
    """
    n = A.rows
    # Copias locales (para no modificar el objeto original)
    M = [row[:] for row in A.data]
    b = b[:]

    # Eliminación
    for k in range(n - 1):
        for i in range(k + 1, n):
            if M[k][k] == 0:
                raise ZeroDivisionError("Pivote cero. Se recomienda usar pivoteo.")
            factor = M[i][k] / M[k][k]
            for j in range(k, n):
                M[i][j] -= factor * M[k][j]
            b[i] -= factor * b[k]

    # Sustitución hacia atrás
    U = Matrix(M)
    return backward_substitution(U, b)


def lu_factorization(A: Matrix):
    """
    Factoriza A = LU (sin pivoteo).
    """
    n = A.rows
    L = [[0 if i != j else 1 for j in range(n)] for i in range(n)]
    U = [row[:] for row in A.data]

    for k in range(n - 1):
        if U[k][k] == 0:
            raise ZeroDivisionError("Pivote cero. Se recomienda usar pivoteo.")
        for i in range(k + 1, n):
            factor = U[i][k] / U[k][k]
            L[i][k] = factor
            for j in range(k, n):
                U[i][j] -= factor * U[k][j]

    return Matrix(L), Matrix(U)


def lu_solve(A: Matrix, b: list) -> list:
    """
    Resuelve Ax = b usando factorización LU.
    """
    L, U = lu_factorization(A)
    y = forward_substitution(L, b)
    x = backward_substitution(U, y)
    return x


# ======================
# Ejemplo de uso
# ======================
if __name__ == "__main__":
    A = Matrix([[2, -1, 1],
                [3, 3, 9],
                [3, 3, 5]])
    b = [2, -1, 4]

    print("Sistema Ax = b")
    print("Matriz A:")
    print(A)
    print("Vector b:", b)

    print("\n--- Gauss ---")
    x_gauss = gaussian_elimination(A, b)
    print("Solución:", x_gauss)

    print("\n--- LU ---")
    x_lu = lu_solve(A, b)
    print("Solución:", x_lu)
