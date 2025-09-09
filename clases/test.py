def calcular_overflow():
    """
    Calcula el valor de overflow para punto flotante.
        
    Returns:
    float: El valor máximo antes del overflow
    """
    valor = 1.0
    valor_previo = 1.0
        
    # Multiplicar por 2 hasta que se produzca overflow (infinito)
    while valor != float('inf'):
        valor_previo = valor
        valor *= 2.0
        
    return valor_previo

print(calcular_overflow())
