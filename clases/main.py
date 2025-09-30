"""
main.py
Script principal para probar la clase Matrix y los métodos de sistemas lineales.
"""

from matrix import Matrix
import linear_systems as ls

def main():
    # Definimos un sistema de prueba
    A = Matrix([[2, -1, 1],
                [3, 3, 9],
                [3, 3, 5]])
    b = [2, -1, 4]

    print("="*60)
    print("Sistema Ax = b")
    print("="*60)
    print("Matriz A:")
    print(A)
    print("Vector b:", b)

    # --- Probar Gaussian Elimination ---
    print("\n--- Eliminación de Gauss ---")
    try:
        x_gauss = ls.gaussian_elimination(A, b)
        print("Solución Gauss:", x_gauss)
    except Exception as e:
        print("Error en main (Gauss):", e)

    # --- Probar LU Factorization ---
    print("\n--- LU Factorization ---")
    try:
        x_lu = ls.lu_solve(A, b)
        print("Solución LU:", x_lu)
    except Exception as e:
        print("Error en main (LU):", e)

if __name__ == "__main__":
    main()

