"""
least_squares_demo.py
---------------------
Script de demostración de Mínimos Cuadrados para la clase.

Incluye:
- Ecuaciones normales
- Sistema aumentado
- Factorización QR (Gram-Schmidt)
- Factorización QR (Householder)
- Verificación de ortogonalidad
- Comparación de métodos

Usa:
    from matrix import Matrix
    from linear_systems import gaussian_elimination, lu_solve
"""
from matrix import Matrix
from linear_systems import gaussian_elimination, lu_solve, backward_substitution
from numerical_tools import mi_raiz_cuadrada as sqrt

# ============================================================
#  - Generación de datos
# ============================================================

def generate_data():
    """
    Genera datos simples: y ≈ 2x + 1 con ruido.
    """
    t = [0, 1, 2, 3, 4, 5]
    y = [1.0, 2.9, 5.1, 6.2, 9.1, 10.2]
    # Matriz A para ajuste lineal: y ≈ a + b*x
    #if len(t) !=  len(y):
    #    raise 
    ###resultado = []
    ###for ti in t:
    ###    rows = 2*[1.0]
    ###    rows[1]=ti
    ###    resultado.append(rows)
    ###
    ###A = Matrix(resultado)
    ###print(A)
    
    A = Matrix([[1.0, ti] for ti in t])
    b = [yi for yi in y]
    return A, b

# ============================================================
# - Normal Equations Method
# ============================================================

def normal_equations(A: Matrix, b: list):
    """
    Resuelve el problema de mínimos cuadrados usando ecuaciones normales:
        (A^T A)x = A^T b
    """
    At = A.transpose()
    AtA = At * AA
    At * b
    Atb = [sum(At.data[i][k] * b[k] for k in range(A.rows)) for i in range(A.cols)]
    return gaussian_elimination(AtA, Atb)

# ============================================================
# - Augmented System Method
# ============================================================

def augmented_system(A: Matrix, b: list):
    """
    Resuelve mínimos cuadrados mediante sistema aumentado:
        [ I   A ] [r]   [b]
        [A^T  0 ] [x] = [0]
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

# ============================================================
#  - QR Factorization (Gram-Schmidt)
# ============================================================

def qr_factorization(A: Matrix, b: list):
    """
    Gram-Schmidt clásico para obtener Q y R,
    luego resolver Rx = Q^T b
    """
    m, n = A.shape()
    Q = [[0.0]*n for _ in range(m)]
    R = [[0.0]*n for _ in range(n)]

    for j in range(n):
        v = [A.data[i][j] for i in range(m)]
        for k in range(j):
            R[k][j] = sum(Q[i][k]*A.data[i][j] for i in range(m))
            v = [v[i] - R[k][j]*Q[i][k] for i in range(m)]
        R[j][j] = sqrt(sum(v[i]**2 for i in range(m)))
        for i in range(m):
            Q[i][j] = v[i] / R[j][j]

    # Resolver Rx = Q^T b
    Qtb = [sum(Q[i][j]*b[i] for i in range(m)) for j in range(n)]
    Rmat = Matrix(R)
    return gaussian_elimination(Rmat, Qtb)

# ============================================================
# - QR Factorization (Householder)
# ============================================================

def qr_householder(A: Matrix, b: list):
    """
    Factorización QR mediante transformaciones de Householder.
    Más estable que Gram-Schmidt.
    """
    A = A.copy()
    m, n = A.shape()
    R = [[A.data[i][j] for j in range(n)] for i in range(m)]
    Q = [[1.0 if i == j else 0.0 for j in range(m)] for i in range(m)]

    for j in range(n):
        # Vector x: columna j de R a partir de fila j
        x = [R[i][j] for i in range(j, m)]
        normx = sqrt(sum(xi**2 for xi in x))
        if normx == 0:
            continue

        # Definimos v = x + sign(x0)*||x||*e1
        sign = 1.0 if x[0] >= 0 else -1.0
        v = [xi for xi in x]
        v[0] += sign * normx
        normv = sqrt(sum(vi**2 for vi in v))
        v = [vi / normv for vi in v]

        # Aplicamos H a R (submatriz desde fila j)
        for c in range(j, n):
            s = sum(v[r] * R[j + r][c] for r in range(len(v)))
            for r in range(len(v)):
                R[j + r][c] -= 2 * v[r] * s

        # Aplicamos H a Q (a toda Q)
        for c in range(m):
            s = sum(v[r] * Q[j + r][c] for r in range(len(v)))
            for r in range(len(v)):
                Q[j + r][c] -= 2 * v[r] * s

    # Transponemos Q
    Q = list(map(list, zip(*Q)))

    # Extraemos R triangular superior
    Rtri = [[0.0]*n for _ in range(n)]
    for i in range(n):
        for j in range(i, n):
            Rtri[i][j] = R[i][j]

    # Resolver Rx = Q^T b
    Qtb = [sum(Q[i][j]*b[i] for i in range(m)) for j in range(n)]
    x = backward_substitution(Matrix(Rtri), Qtb)
    return x

# ============================================================
# - Verificación de Ortogonalidad
# ============================================================

def check_orthogonality(A: Matrix, x: list, b: list):
    """Verifica que el residuo r = b - A x sea ortogonal a las columnas de A."""
    r = [b[i] - sum(A.data[i][j]*x[j] for j in range(A.cols)) for i in range(A.rows)]
    At = A.transpose()
    Atr = [sum(At.data[i][k]*r[k] for k in range(A.rows)) for i in range(A.cols)]
    print("\nVerificación de ortogonalidad:")
    for i, val in enumerate(Atr):
        print(f"A^T r componente {i} approx {val:.3e}")

# ============================================================
# - Comparación de Métodos
# ============================================================

def compare_methods(A: Matrix, b: list):
    """
    Compara los métodos y muestra los errores residuales.
    """
    from math import sqrt
    methods = {
        "Normal Equations": normal_equations,
        "Augmented System": augmented_system,
        "QR (Gram-Schmidt)": qr_factorization,
        "QR (Householder)": qr_householder
    }

    print("\n--- Comparación de métodos ---")
    for name, method in methods.items():
        x = method(A, b)
        r = [b[i] - sum(A.data[i][j]*x[j] for j in range(A.cols)) for i in range(A.rows)]
        error = sqrt(sum(ri**2 for ri in r))
        print(f"{name:20s} -> ||r||_2 = {error:.3e}, x = {[round(v,3) for v in x]}")

# ============================================================
# Ejecución principal
# ============================================================

def main():
    A, b = generate_data()

    print("Matriz A:")
    print(A)
    print("\nVector b:", b)

    ##### Método 1: Ecuaciones normales
    ####x_ne = normal_equations(A, b)
    ####print("\n--- Normal Equations ---")
    ####print("Coeficientes:", x_ne)

    ##### Método 2: Sistema aumentado
    ####x_aug = augmented_system(A, b)
    ####print("\n--- Augmented System ---")
    ####print("Coeficientes:", x_aug)

    ##### Método 3: QR (Gram-Schmidt)
    ####x_qr = qr_factorization(A, b)
    ####print("\n--- QR (Gram-Schmidt) ---")
    ####print("Coeficientes:", x_qr)

    ##### Método 4: QR (Householder)
    ####x_h = qr_householder(A, b)
    ####print("\n--- QR (Householder) ---")
    ####print("Coeficientes:", x_h)

    ##### Verificación ortogonalidad
    ####check_orthogonality(A, x_qr, b)

    ##### Comparación final
    ####compare_methods(A, b)


if __name__ == "__main__":
    main()

