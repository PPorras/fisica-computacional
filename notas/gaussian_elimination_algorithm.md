# ALGORITMO Y EJEMPLOS

Para resumir el método de **eliminación Gaussiana completa con sustitución hacia atrás**, se presenta el siguiente algoritmo.

---

## Algoritmo de eliminación Gaussiana con sustitución hacia atrás

### Objetivo
Resolver el sistema lineal de \( n \times n \):

$$
\begin{aligned}
E_1 &: a_{11} x_1 + a_{12} x_2 + \dots + a_{1n} x_n = a_{1,n+1} \\
E_2 &: a_{21} x_1 + a_{22} x_2 + \dots + a_{2n} x_n = a_{2,n+1} \\
&\vdots \\
E_n &: a_{n1} x_1 + a_{n2} x_2 + \dots + a_{nn} x_n = a_{n,n+1}
\end{aligned}
$$

---

### Datos de entrada
- **n**: número de incógnitas y de ecuaciones.
- **Matriz ampliada** $ A_a = (a_{ij}) $, donde $ 1 \le i \le n $ y $ 1 \le j \le n + 1 $.

### Salida
- Solución $x_1, x_2, \dots, x_n $,  
  o mensaje indicando que **el sistema lineal no tiene solución única**.

---

## Procedimiento paso a paso

### Paso 1:
Para $i = 1, 2, \dots, n - 1 $, seguir los pasos 2–4 (proceso de eliminación).

### Paso 2:
Sea $p$ el menor entero con  $i \le p \le n$ y $ a_{pi} \ne 0 $.  
Si **no existe tal p**, **SALIDA** → no existe solución única. **PARAR.**

### Paso 3:
Si $ p \ne i $, entonces **intercambiar las ecuaciones**:  
$$
(E_p) \leftrightarrow (E_i)
$$

### Paso 4:
Para $j = i + 1, i + 2, \dots, n $, seguir los pasos 5 y 6.

### Paso 5:
Calcular el **multiplicador**:
$$
m_{ji} = \frac{a_{ji}}{a_{ii}}
$$

### Paso 6:
Efectuar la **operación de eliminación**:
$$
(E_j - m_{ji} E_i) \to (E_j)
$$

---

### Paso 7:
Si $ a_{nn} = 0$, entonces **SALIDA** → no existe solución única. **PARAR.**

---

## Sustitución hacia atrás

### Paso 8:
Comenzar la sustitución hacia atrás.  
Calcular:
$$
x_n = \frac{a_{n, n+1}}{a_{nn}}
$$

### Paso 9:
Para $ i = n - 1, n - 2, \dots, 1 $, calcular:
$$
x_i = \frac{a_{i, n+1} - \sum_{j=i+1}^{n} a_{ij} x_j}{a_{ii}}
$$

---

### Paso 10:
**SALIDA:**  
$$
(x_1, x_2, \dots, x_n)
$$

(procedimiento completado satisfactoriamente)

---

**Fin del algoritmo.**

---

### Notas
- Este método es la base de los algoritmos modernos de factorización LU.  
- La **eliminación hacia adelante** (pasos 1–6) transforma el sistema en uno **triangular superior**.  
- La **sustitución hacia atrás** (pasos 8–9) obtiene las incógnitas una por una.  
- Si se detecta un pivote nulo (\( a_{ii} = 0 \)), el sistema **no tiene solución única** o requiere **pivoteo** para continuar.

---

