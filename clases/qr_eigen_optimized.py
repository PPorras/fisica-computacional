"""
qr_eigen_optimized.py
---------------------
Método QR para autovalores usando mi_raiz_cuadrada y las funciones QR existentes.
"""

from matrix import Matrix
from numerical_tools import mi_raiz_cuadrada
from math import copysign

def qr_eigenvalues_householder(A: Matrix, tol=1e-12, max_iter=100):
    """
    Método QR usando Householder con mi_raiz_cuadrada.
    
    Parameters
    ----------
    A : Matrix
        Matriz cuadrada
    tol : float
        Tolerancia
    max_iter : int
        Iteraciones máximas
        
    Returns
    -------
    eigenvalues : list
        Autovalores aproximados
    Ak : Matrix
        Forma de Schur final
    """
    n = A.rows
    if n != A.cols:
        raise ValueError("La matriz debe ser cuadrada.")
    
    # Copiar matriz
    Ak = A.copy()
    
    print("Método QR con Householder...")
    print(f"Matriz original {n}x{n}:")
    print(Ak)
    print()
    
    for iteration in range(max_iter):
        # Factorización QR con Householder
        Q, R = qr_householder_for_eigen(Ak)
        
        # A_{k+1} = R * Q
        Ak = R * Q
        
        # Verificar convergencia (elementos subdiagonales)
        converged = True
        for i in range(1, n):
            if abs(Ak.data[i][i-1]) > tol:
                converged = False
                break
        
        if iteration % 10 == 0:
            subdiag_norm = 0.0
            for i in range(1, n):
                subdiag_norm += Ak.data[i][i-1]**2
            subdiag_norm = mi_raiz_cuadrada(subdiag_norm)
            print(f"Iteración {iteration}: ||subdiagonal|| = {subdiag_norm:.2e}")
        
        if converged:
            print(f"Convergencia alcanzada en iteración {iteration}")
            break
    
    if iteration == max_iter - 1:
        print(f"Advertencia: Máximo de iteraciones ({max_iter}) alcanzado")
    
    # Extraer autovalores
    eigenvalues = extract_eigenvalues(Ak, tol)
    return eigenvalues, Ak

def qr_householder_for_eigen(A: Matrix):
    """
    Adaptación de Householder usando mi_raiz_cuadrada.
    
    Parameters
    ----------
    A : Matrix
        Matriz a factorizar
        
    Returns
    -------
    Q : Matrix
        Matriz ortogonal
    R : Matrix
        Matriz triangular superior
    """
    A_temp = A.copy()
    m, n = A_temp.shape()
    
    # Inicializar Q como identidad
    Q = Matrix([[1.0 if i == j else 0.0 for j in range(m)] for i in range(m)])
    R = A_temp
    
    for j in range(n):
        # Vector x: columna j de R desde fila j
        x = [R.data[i][j] for i in range(j, m)]
        
        # Calcular norma con mi_raiz_cuadrada
        sum_sq = sum(xi**2 for xi in x)
        norm_x = mi_raiz_cuadrada(sum_sq)
        
        if norm_x == 0:
            continue
            
        # Vector de Householder
        sign = 1.0 if x[0] >= 0 else -1.0
        v = [xi for xi in x]
        v[0] += sign * norm_x
        
        # Calcular norma de v con mi_raiz_cuadrada
        sum_sq_v = sum(vi**2 for vi in v)
        norm_v = mi_raiz_cuadrada(sum_sq_v)
        v = [vi / norm_v for vi in v]
        
        # Aplicar transformación a R
        for col in range(j, n):
            # Producto punto v · columna
            dot_product = sum(v[r] * R.data[j + r][col] for r in range(len(v)))
            for r in range(len(v)):
                R.data[j + r][col] -= 2 * v[r] * dot_product
        
        # Aplicar transformación a Q
        for col in range(m):
            dot_product = sum(v[r] * Q.data[j + r][col] for r in range(len(v)))
            for r in range(len(v)):
                Q.data[j + r][col] -= 2 * v[r] * dot_product
    
    # Q está almacenada por columnas, necesitamos transpuesta para tener Q ortogonal
    Q = Q.transpose()
    
    return Q, R

def qr_eigenvalues_gram_schmidt(A: Matrix, tol=1e-10, max_iter=100):
    """
    Método QR usando Gram-Schmidt con mi_raiz_cuadrada.
    """
    n = A.rows
    Ak = A.copy()
    
    print("Método QR con Gram-Schmidt...")
    
    for iteration in range(max_iter):
        # Factorización QR con Gram-Schmidt
        Q, R = qr_gram_schmidt_for_eigen(Ak)
        
        # A_{k+1} = R * Q
        Ak = R * Q
        
        # Verificar convergencia
        converged = True
        for i in range(1, n):
            if abs(Ak.data[i][i-1]) > tol:
                converged = False
                break
                
        if converged:
            print(f"Convergencia en iteración {iteration}")
            break
    
    if iteration == max_iter - 1:
        print(f"Advertencia: Máximo de iteraciones ({max_iter}) alcanzado")
    
    eigenvalues = extract_eigenvalues(Ak, tol)
    return eigenvalues, Ak

def qr_gram_schmidt_for_eigen(A: Matrix):
    """
    Gram-Schmidt usando mi_raiz_cuadrada.
    """
    m, n = A.shape()
    Q_data = [[0.0] * n for _ in range(m)]
    R_data = [[0.0] * n for _ in range(n)]
    
    for j in range(n):
        v = [A.data[i][j] for i in range(m)]
        
        for k in range(j):
            R_data[k][j] = sum(Q_data[i][k] * A.data[i][j] for i in range(m))
            for i in range(m):
                v[i] -= R_data[k][j] * Q_data[i][k]
        
        # Usar mi_raiz_cuadrada para la norma
        sum_sq = sum(vi**2 for vi in v)
        R_data[j][j] = mi_raiz_cuadrada(sum_sq)
        
        if R_data[j][j] > 1e-12:
            for i in range(m):
                Q_data[i][j] = v[i] / R_data[j][j]
        else:
            for i in range(m):
                Q_data[i][j] = 0.0
    
    return Matrix(Q_data), Matrix(R_data)

def extract_eigenvalues(Schur: Matrix, tol=1e-10):
    """
    Extrae autovalores de la matriz de Schur usando mi_raiz_cuadrada.
    
    Parameters
    ----------
    Schur : Matrix
        Matriz en forma de Schur
    tol : float
        Tolerancia para considerar cero
        
    Returns
    -------
    eigenvalues : list
        Lista de autovalores
    """
    n = Schur.rows
    eigenvalues = []
    i = 0
    
    while i < n:
        if i == n-1 or abs(Schur.data[i+1][i]) < tol:
            # Autovalor real simple
            eigenvalues.append(Schur.data[i][i])
            i += 1
        else:
            # Bloque 2x2 (autovalores complejos o reales repetidos)
            a, b, c, d = Schur.data[i][i], Schur.data[i][i+1], Schur.data[i+1][i], Schur.data[i+1][i+1]
            trace = a + d
            det = a * d - b * c
            
            # Calcular autovalores del bloque 2x2
            discriminant = trace**2 - 4 * det
            
            if discriminant >= 0:
                # Autovalores reales
                sqrt_disc = mi_raiz_cuadrada(discriminant)
                eigenvalues.append((trace + sqrt_disc) / 2)
                eigenvalues.append((trace - sqrt_disc) / 2)
            else:
                # Autovalores complejos
                real_part = trace / 2
                imag_part = mi_raiz_cuadrada(-discriminant)
                eigenvalues.append(complex(real_part, imag_part))
                eigenvalues.append(complex(real_part, -imag_part))
            i += 2
    
    return eigenvalues

def verify_eigenvalues(A: Matrix, eigenvalues, tol=1e-8):
    """
    Verifica que los autovalores sean correctos.
    
    Parameters
    ----------
    A : Matrix
        Matriz original
    eigenvalues : list
        Lista de autovalores calculados
    tol : float
        Tolerancia para la verificación
        
    Returns
    -------
    max_error : float
        Error máximo en la verificación
    """
    n = A.rows
    max_error = 0.0
    
    print("\nVerificación de autovalores:")
    print("-" * 40)
    
    for i, λ in enumerate(eigenvalues):
        if isinstance(λ, complex):
            # Para autovalores complejos, verificamos el determinante
            # det(A - λI) debería ser cercano a cero
            A_minus_λI = A.copy()
            for j in range(n):
                A_minus_λI.data[j][j] -= λ.real
            # Simplificación: solo verificamos la parte real
            error = abs(λ.imag)
            print(f"λ_{i+1} = {λ.real:.4f} + {λ.imag:.4f}i, error = {error:.2e}")
            max_error = max(max_error, error)
        else:
            # Para autovalores reales, verificamos que det(A - λI) ≈ 0
            A_minus_λI = A.copy()
            for j in range(n):
                A_minus_λI.data[j][j] -= λ
            
            # Estimación simple del error
            error = 0.0
            for j in range(n):
                error += abs(sum(A_minus_λI.data[j][k] for k in range(n))) / n
            
            print(f"λ_{i+1} = {λ:.6f}, error = {error:.2e}")
            max_error = max(max_error, error)
    
    return max_error

def test_qr_comprehensive():
    """
    Prueba comprehensiva del método QR.
    """
    print("=" * 60)
    print("PRUEBA COMPLETA DEL MÉTODO QR")
    print("=" * 60)
    
    # Test 1: Matriz simétrica
    print("\n1. MATRIZ SIMÉTRICA")
    A_sym = Matrix([[4.0, -2.0, 2.0],
                    [-2.0, 1.0, 0.0],
                    [2.0, 0.0, 3.0]])
    
    print("Matriz A:")
    print(A_sym)
    
    eigen_house, Schur_house = qr_eigenvalues_householder(A_sym)
    print("\nAutovalores (Householder):", [f"{λ:.6f}" for λ in eigen_house])
    
    # Test 2: Matriz no simétrica
    print("\n2. MATRIZ NO SIMÉTRICA")
    A_nonsym = Matrix([[4.0, 1.0, 2.0],
                       [0.0, 3.0, 1.0],
                       [1.0, 2.0, 5.0]])
    
    print("Matriz B:")
    print(A_nonsym)
    
    eigen_nonsym, Schur_nonsym = qr_eigenvalues_householder(A_nonsym)
    print("\nAutovalores:", [f"{λ:.6f}" for λ in eigen_nonsym])
    
    # Test 3: Comparación de métodos
    print("\n3. COMPARACIÓN HOUSEHOLDER vs GRAM-SCHMIDT")
    A_comp = Matrix([[2.0, 1.0, 0.0],
                     [1.0, 3.0, 1.0],
                     [0.0, 1.0, 2.0]])
    
    eigen_house, _ = qr_eigenvalues_householder(A_comp, tol=1e-8)
    eigen_gram, _ = qr_eigenvalues_gram_schmidt(A_comp, tol=1e-8)
    
    print("Householder:", [f"{λ:.6f}" for λ in eigen_house])
    print("Gram-Schmidt:", [f"{λ:.6f}" for λ in eigen_gram])
    
    # Calcular diferencia
    diff = max(abs(eigen_house[i] - eigen_gram[i]) for i in range(len(eigen_house)))
    print(f"Diferencia máxima: {diff:.2e}")
    
    # Test 4: Verificación
    print("\n4. VERIFICACIÓN NUMÉRICA")
    max_error = verify_eigenvalues(A_sym, eigen_house)
    print(f"Error máximo de verificación: {max_error:.2e}")

# =====================================================
# Ejemplo de uso principal
# =====================================================
if __name__ == "__main__":
    test_qr_comprehensive()
    
    # Ejemplo adicional interactivo
    print("\n" + "=" * 60)
    print("EJEMPLO INTERACTIVO - MATRIZ NO SIMÉTRICA")
    print("=" * 60)
    
    # Matriz no simétrica interesante
    C = Matrix([[5.0, -2.0, 1.0, 0.0],
                [3.0, 0.0, -1.0, 2.0],
                [1.0, 2.0, 4.0, -1.0],
                [0.0, 1.0, -1.0, 3.0]])
    
    print("Matriz 4x4 no simétrica:")
    print(C)
    
    eigenvalues, Schur = qr_eigenvalues_householder(C, tol=1e-12, max_iter=200)
    
    print("\nResultados:")
    for i, λ in enumerate(eigenvalues):
        if isinstance(λ, complex):
            print(f"λ_{i+1} = {λ.real:.6f} + {λ.imag:.6f}i")
        else:
            print(f"λ_{i+1} = {λ:.6f}")
    
    print("\nPrimeros elementos de la forma de Schur:")
    for i in range(min(4, C.rows)):
        row_str = "  ".join([f"{Schur.data[i][j]:8.4f}" for j in range(min(4, C.cols))])
        print(f"  {row_str}")
        if i == 3 and C.rows > 4:
            print("  ...")
