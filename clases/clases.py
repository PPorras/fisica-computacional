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
    def __repr__(self):
        return f"Vector3D({self.x}, {self.y}, {self.z})"


    def norm(self):
        """Devuelve la norma euclídea"""
        return (self.x**2 + self.y**2 + self.z**2) ** 0.5

    def __add__(self, other):
        """Suma de vectores"""
        return Vector3D(self.x + other.x,
                        self.y + other.y,
                        self.z + other.z)

    def dot(self, other):
        """Producto escalar"""
        return self.x * other.x + self.y * other.y + self.z * other.z

    def __rmul__(self, scalar):
        """Multiplicación por escalar (scalar * v)"""
        return Vector3D(scalar * self.x,
                        scalar * self.y,
                        scalar * self.z)



# ----------------------------
# PARTE 2: VectorND (para hacer en clase)
# ----------------------------
class VectorND:
    def __init__(self, coords):
        # TODO: guardar coords como lista en self.coords (atributo)
        pass

    def __repr__(self):
        # TODO: devolver un string tipo "VectorND([1,2,3])"
        pass

    def norm(self):
        """Devuelve la norma euclídea"""
        # TODO: usar sumatoria de c**2 para c en self.coords
        pass

    def __add__(self, other):
        """Suma de vectores"""
        # TODO: checar que las dimensiones coincidan
        # TODO: devolver un nuevo VectorND con la suma coordenada a coordenada
        pass

    def dot(self, other):
        """Producto escalar"""
        # TODO: checar dimensiones
        # TODO: devolver suma de a*b para cada par (a,b) en zip(...)
        pass

    def __rmul__(self, scalar):
        """Multiplicación por escalar (scalar * v)"""
        # TODO: devolver nuevo VectorND con scalar * cada coordenada
        pass


# ----------------------------
# MAIN: solo se ejecuta si corres el script directamente
# ----------------------------
if __name__ == "__main__":
    print("=== Vector3D (resuelto) ===")
    v1 = Vector3D(1, 2, 3)
    v2 = Vector3D(4, 5, 6)

    print("v1:", v1)
    print("v2:", v2)
    print("Norma de v1:", v1.norm())
    print("Suma:", v1 + v2)
    print("Producto escalar:", v1.dot(v2))
    print("2 * v1:", 2 * v1)
    print()

    print("=== VectorND (por completar en clase) ===")
    # Cuando terminen la implementación, este código debe funcionar:
    # v1 = VectorND([1, 2, 3])
    # v2 = VectorND([4, 5, 6])
    # print("v1:", v1)
    # print("v2:", v2)
    # print("Norma de v1:", v1.norm())
    # print("Suma:", v1 + v2)
    # print("Producto escalar:", v1.dot(v2))
    # print("2 * v1:", 2 * v1)

