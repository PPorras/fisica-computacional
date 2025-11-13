"""
power_utils.py
--------------

Funciones auxiliares para el método de la potencia y deflación.

Requiere:
    - matrix.py
    - numerical_tools.py
"""

from matrix import Matrix
from numerical_tools import mi_raiz_cuadrada


def vector_norm(v):
    """Norma euclídea de un vector (usa mi_raiz_cuadrada)."""
    suma = sum(x**2 for x in v)
    return mi_raiz_cuadrada(suma)


def normalize(v):
    """Devuelve el vector normalizado."""
    norm = vector_norm(v)
    if norm == 0:
        raise ValueError("El vector tiene norma cero.")
    return [x / norm for x in v]


def matrix_vector_product(A, v):
    """Multiplica la matriz A (Matrix) por el vector v (lista)."""
    result = []
    for i in range(A.rows):
        suma = sum(A.data[i][j] * v[j] for j in range(A.cols))
        result.append(suma)
    return result


def outer_product(v, w):
    """Producto exterior v * w^T."""
    n = len(v)
    m = len(w)
    return Matrix([[v[i] * w[j] for j in range(m)] for i in range(n)])


def vector_add(a, b):
    return [ai + bi for ai, bi in zip(a, b)]


def vector_sub(a, b):
    return [ai - bi for ai, bi in zip(a, b)]


def vector_scale(a, s):
    return [s * ai for ai in a]


def vector_norm(a):
    return sum(x*x for x in a) ** 0.5
