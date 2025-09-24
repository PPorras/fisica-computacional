#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
matrix.py
----------

Este módulo define la clase Matrix para representar matrices y realizar operaciones básicas

Incluye:
- Creación de matrices a partir de listas de listas.
- Suma, resta y multiplicación (escalar y matricial).
- Transpuesta.
- Métodos auxiliares para acceder a filas y columnas.

Los métodos están preparados con `TODO` para completar en clase.
"""

class Matrix:
    """
    Clase para representar matrices y operaciones básicas.

    Attributes
    ----------
    data : list of list of numbers
        Almacena los elementos de la matriz.
    rows : int
        Número de filas.
    cols : int
        Número de columnas.

    Methods
    -------
    shape():
        Devuelve una tupla con la dimensión de la matriz (filas, columnas).
    get_row(i):
        Devuelve la fila i (0-indexada).
    get_col(j):
        Devuelve la columna j (0-indexada).
    transpose():
        Devuelve la matriz transpuesta.
    __add__(other):
        Suma dos matrices del mismo tamaño.
    __sub__(other):
        Resta dos matrices del mismo tamaño.
    __mul__(other):
        Multiplica la matriz por un escalar o por otra matriz.
    """

    def __init__(self, data):
        """
        Inicializa una matriz a partir de una lista de listas.

        Parameters
        ----------
        data : list of list of numbers
            Lista de listas rectangular con los valores de la matriz.

        Raises
        ------
        ValueError
            Si las filas no tienen la misma longitud.
        """
        if not all(len(data[0]) == len(row) for row in data):
             raise ValueError("Todas las filas deben tener la misma longitud.")
        
        self.data = [list(row) for row in data]
        self.rows = len(data)
        self.cols = len(data[0])

    def __str__(self):
        """Representación bonita para impresión."""
        return "\n".join(["\t".join(map(str, row)) for row in self.data])

    def shape(self):
        """Devuelve la dimensión de la matriz como (filas, columnas)."""
        return (self.rows, self.cols)

    def get_row(self, i):
        """Devuelve la fila i (0-indexada)."""
        if self.rows <= i:
             raise ValueError("Índice fuera de rango.")

        return self.data[i]
        # TODO: retornar fila i

    def get_col(self, j):
        """Devuelve la columna j (0-indexada)."""
        if self.cols <= j:
             raise ValueError("Índice fuera de rango.")
        ##columns = []
        ##for row in self.data:
        ##    columns.append(row[j])
        return [row[j] for row in self.data]

    def __add__(self, other):
        """Suma de matrices del mismo tamaño."""
        if self.shape() != other.shape():
            raise ValueError("Las matrices deben tener las mismas dimensiones.")
        ####resultado = []
        ####for row1, row2 in zip(self.data, other.data):
        ####    newrow = []

        ####    for comp1, comp2 in zip(row1, row2):
        ####        suma =  comp1 + comp2
        ####        newrow.append(suma)

        ####    resultado.append(newrow)
        ####    
        ##return Matrix(resultado) 
        return Matrix([[self.data[i][j] + other.data[i][j] 
                    for j in range(self.cols)] for i in range(self.rows)])

    def __sub__(self, other):
        """Resta de matrices del mismo tamaño."""
        # TODO: verificar que tengan misma dimensión
        # TODO: construir nueva matriz con la resta elemento a elemento
        # raise ValueError si las dimensiones no coinciden
        pass

    def __mul__(self, other):
        """
        Multiplicación por escalar o por otra matriz.

        Parameters
        ----------
        other : int, float, Matrix
            Escalar o matriz a multiplicar.

        Returns
        -------
        Matrix
            Nueva matriz con el resultado.

        Raises
        ------
        ValueError
            Si las dimensiones no son compatibles en multiplicación matricial.
        TypeError
            Si el tipo de `other` no es soportado.
        """

        if isinstance(other,(int, float)):
            ###resultado = []
            ###for i in range(self.rows):
            ###    newrow = []
            ###    for j in range(self.cols):
            ###        aux = self.data[i][j]*other
            ###        newrow.append(aux)
            ###    resultado.append(newrow)
            ###return Matrix(resultado)
            return Matrix([[self.data[i][j]*other for j in range(self.cols)] for i in range(self.rows)])

        elif isinstance(othet, Matrx):
            for i in range(self.rows):
                     
        # TODO: Si other es escalar, multiplicar cada elemento
        # TODO: Si other es Matrix, verificar compatibilidad de dimensiones
        # TODO: Implementar multiplicación matricial con suma de productos
        # TODO: raise TypeError si no es válido
        ##pass

    def transpose(self):
        """Devuelve la transpuesta de la matriz."""
        # TODO: intercambiar filas por columnas
        pass


# ======================
# Ejemplo de uso
# ======================
if __name__ == "__main__":
    # TODO: Completar pruebas en clase

    A = Matrix([[1, 2, 3],
                [4, 5, 6]])
    print(f'Las componetes de la matriz A son{A.data}')
    print(f'La matriz A, tienen {A.rows}, renglones')
    print(f'La matriz A, tienen {A.cols}, colmnas')

    B = Matrix([[7, 8, 9],
                [10, 11, 12]])

    print("Matriz A:")
    print(A)
    print(f'La forma dela matriz A es {A.shape()}')
    print(f'El primer renglón de la matriz A es {A.get_row(0)}')
    print(f'El primer renglón de la matriz A es {A.get_row(1)}')
    print(f'La primera columna de la matriz A es {A.get_col(1)}')

    print("\nMatriz B:")
    print(B)

    print("\nA + B:")
    print(A + B)   # TODO: implementar suma

    print("\nA * 2 (escalar):")
    ###print(A * 2)   # TODO: implementar multiplicación por escalar
    print(A * 2.0)   # TODO: implementar multiplicación por escalar
####
####    C = Matrix([[1, 2],
####                [3, 4],
####                [5, 6]])
####    print("\nA * C (matricial):")
####    print(A * C)   # TODO: implementar multiplicación de matrices
####
####    print("\nTranspuesta de A:")
####    print(A.transpose())   # TODO: implementar transpuesta
####
