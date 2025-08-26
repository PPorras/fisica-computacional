def isPrime(number: int) -> bool:
    """
    Verifica si un número es primo.

    Args:
        number (int): Número a verificar.
        
    Returns:
        bool: True si es primo, False si no lo es.

    Raises:
        TypeError: Si la entrada no es un entero.
    """
    # Verificar tipo
    if not isinstance(number, int):
        raise TypeError(f"Se esperaba un int, pero se recibió {type(number).__name__}")


    if number <= 1:
        return False
    elif number == 2:
        return True
    elif number % 2 == 0:
        return False

    # Verificar divisibilidad por números impares
    for i in range(3, int(number**0.5) + 1, 2):
        if number % i == 0:
            return False
    return True
