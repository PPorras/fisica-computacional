# ==============================================================
# Mini clase de POO con Python: Vectores
# ==============================================================

"""
En Programación Orientada a Objetos (POO) cada clase tiene:

- Atributos: son las "propiedades" o "datos" que describen al objeto.
  Ejemplo: las coordenadas de un vector (x, y, z).

- Métodos: son las "acciones" o "comportamientos" que puede realizar
  el objeto. Son funciones definidas dentro de la clase.
  Ejemplo: calcular la norma, sumar dos vectores, hacer un producto escalar.

Regla general:
    * Los atributos son "sustantivos".
    * Los métodos son "verbos".
"""

# ----------------------------
# PARTE 1: Vector 3D (resuelto)
# ----------------------------
class Vector3D:
    def __init__(self, x, y, z):
        # ==== ATRIBUTOS ====
        self.x = x
        self.y = y
        self.z = z

    # ==== MÉTODOS ====
    ##def imprimir(self):
    #    return print(f"JVector3D({self.x}, {self.y}, {self.z})")

    def __repr__(self):
        return f"Vector3D({self.x}, {self.y}, {self.z})"

    def __add__(self, other):
        """Suma de vectores"""
        return Vector3D(self.x + other.x,
                        self.y + other.y,
                        self.z + other.z)

    def __rmul__(self, scalar):
        """Multiplicación por escalar (scalar * v)"""
        return Vector3D(scalar * self.x,
                        scalar * self.y,
                        scalar * self.z)
    def dot(self, other):
        """Producto escalar"""
        return self.x * other.x + self.y * other.y + self.z * other.z

    def norm(self):
        """Devuelve la norma euclídea"""
        return self.dot(self)**0.5
# ----------------------------
# PARTE 2: VectorND (para hacer en clase)
# ----------------------------
class VectorND:
    def __init__(self, coords):
        self.coords = list(coords)

    def __repr__(self):
        return f"VectorND({self.coords})"

    def __add__(self, other):
        if len(self.coords) != len(other.coords):
            raise ValueError("Las dimensiones no son iguales")

        return VectorND([a + b for a,b in zip(self.coords, other.coords)] )

    def __rmul__(self, scalar):
        """Multiplicación por escalar (scalar * v)"""
        # TODO: devolver nuevo VectorND con scalar * cada coordenada
        pass

    def dot(self, other):
        """Producto escalar"""
        # TODO: checar dimensiones
        # TODO: devolver suma de a*b para cada par (a,b) en zip(...)
        pass
    def norm(self):
        """Devuelve la norma euclídea"""
        # TODO: usar suma de c**2 para c en self.coords
        pass





# ----------------------------
# MAIN: solo se ejecuta si corres el script directamente
# ----------------------------
if __name__ == "__main__":
    print("=== Vector3D (resuelto) ===")
    v1 = Vector3D(1, 2, 3)
    print(f'La componentes de vector "v1" son {v1.x},{v1.y},{v1.z}')
    v2 = Vector3D(4, 5, 6)
    print(f'El vector v1 es:, {v1}')
    print(f'El vector v2 es: {v2}')
    print(f'La suma de v1 más v2 es: {v1 + v2}')
    print(f'La producto por escalar 2.0*v1 es: {2*v1}')
    print(f'La producto punto v1*v2 es: {v1.dot(v2)}')
    print(f'La norma de v1 es: {v1.norm()}')

    print("=== VectorND (por completar en clase) ===")
    # Cuando terminen la implementación, este código debe funcionar:
    v1 = VectorND([1, 2, 3])
    v2 = VectorND([4, 5, 6])
    print(v1)
    print(v2)
    print("Suma:", v1 + v2)
    # print("v1:", v1)
    # print("v2:", v2)
    # print("Norma de v1:", v1.norm())
    # print("Producto escalar:", v1.dot(v2))
    # print("2 * v1:", 2 * v1)

