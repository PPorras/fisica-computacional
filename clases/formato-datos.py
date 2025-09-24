# Script demostrativo para clase

def explicar_proceso(data):
    print("=== EXPLICACIÓN PASO A PASO ===\n")
    
    print("1. MATRIZ ORIGINAL:")
    for i, fila in enumerate(data):
        print(f"   Fila {i}: {fila}")
    
    print("\n2. CONVERSIÓN A TEXTO (map str):")
    for fila in data:
        convertido = list(map(str, fila))
        print(f"   {fila} a {convertido}")
    
    print("\n3. UNIR COLUMNAS CON TABS:")
    filas_procesadas = []
    for fila in data:
        fila_unida = "\t".join(map(str, fila))
        filas_procesadas.append(fila_unida)
        print(f"   '{fila_unida}'")
    
    print("\n4. UNIR FILAS CON SALTOS DE LÍNEA:")
    resultado = "\n".join(filas_procesadas)
    print("   Resultado final:")
    print("   --- INICIO ---")
    print(resultado)
    print("   --- FIN ---")
    
    return resultado

# Datos de ejemplo
data = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Ejecutar explicación
resultado = explicar_proceso(data)

# Mostrar la línea completa
print(f"\n=== LÍNEA COMPLETA ===")
print('resultado = "\\n".join(["\\t".join(map(str, row)) for row in data])')
