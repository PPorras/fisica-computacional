# FACTORIZACIÓN LU

La **factorización LU** (también llamada **descomposición LU**) es un método directo para resolver sistemas lineales de ecuaciones de la forma:

\[
A \, x = b
\]

donde \( A \) es una matriz cuadrada no singular.  
El método consiste en **factorizar la matriz \( A \)** en el producto de una matriz triangular inferior \( L \) y una matriz triangular superior \( U \):

\[
A = L \, U
\]

donde:
- \( L = (l_{ij}) \) es una matriz **triangular inferior** con unos en su diagonal principal (\( l_{ii} = 1 \)),
- \( U = (u_{ij}) \) es una matriz **triangular superior**.

El sistema \( A x = b \) puede resolverse en dos pasos:

1. Resolver el sistema **triangular inferior** \( L y = b \) (sustitución hacia adelante).  
2. Resolver el sistema **triangular superior** \( U x = y \) (sustitución hacia atrás).

---

## Algoritmo de Factorización LU
==================================================

### Entrada:
- Dimensión \( n \)
- Elementos \( a_{ij} \), \( 1 \le i,j \le n \), de la matriz \( A \)

### Salida:
- Elementos \( l_{ij} \) de la matriz \( L \)
- Elementos \( u_{ij} \) de la matriz \( U \)

---

### Paso 1:
Inicializar:
\[
l_{ii} = 1, \quad \text{para todo } i = 1, 2, \dots, n
\]

---

### Paso 2:
Para \( k = 1, 2, \dots, n \):

#### (a) Calcular los elementos de la fila \( k \) de \( U \):
\[
u_{kj} = a_{kj} - \sum_{p=1}^{k-1} l_{kp} u_{pj}, \quad \text{para } j = k, k+1, \dots, n
\]

#### (b) Calcular los elementos de la columna \( k \) de \( L \):
\[
l_{ik} = \frac{1}{u_{kk}} \left( a_{ik} - \sum_{p=1}^{k-1} l_{ip} u_{pk} \right), \quad \text{para } i = k+1, k+2, \dots, n
\]

Si \( u_{kk} = 0 \), la factorización LU **no es posible** sin intercambio de filas (pivotamiento).

---

### Paso 3:
Obtenidas las matrices \( L \) y \( U \), resolver:

1. **Sustitución hacia adelante:**
   \[
   L y = b
   \]
   para encontrar el vector intermedio \( y \).

2. **Sustitución hacia atrás:**
   \[
   U x = y
   \]
   para obtener la solución \( x \).

---

### Paso 4 (Opcional): Pivotamiento parcial

Si durante el proceso se cumple que \( u_{kk} = 0 \) o es muy pequeño, se debe realizar un **pivotamiento parcial**:
- Intercambiar la fila \( k \) de \( A \) con una fila posterior \( p \) tal que \( |a_{pk}| \) sea máximo.
- Intercambiar también las filas correspondientes en \( b \) y en \( L \).

Esto mejora la estabilidad numérica y evita divisiones por cero.

---

### Resultado Final:
\[
A = L \, U, \quad \text{donde } L \text{ es triangular inferior y } U \text{ triangular superior.}
\]

---

### Ejemplo Numérico

Sea:
\[
A = 
\begin{bmatrix}
2 & 3 & 1 \\
4 & 7 & 7 \\
-2 & 4 & 5
\end{bmatrix}
\]

El procedimiento produce:

\[
L = 
\begin{bmatrix}
1 & 0 & 0 \\
2 & 1 & 0 \\
-1 & 2 & 1
\end{bmatrix}, \quad
U =
\begin{bmatrix}
2 & 3 & 1 \\
0 & 1 & 5 \\
0 & 0 & -6
\end{bmatrix}
\]

y se verifica que \( A = L \, U \).

==================================================

