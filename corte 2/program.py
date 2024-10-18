from functools import reduce

# Lista de números
numeros = [1, 3, 6, 9, 12, 15, 17, 20, 23, 26]

# Función para verificar si un número es impar
def es_impar(x):
    return x % 2 != 0

# Función para elevar al cuadrado
def cuadrado(x):
    return x ** 2

# Filtramos los números impares
numeros_impares = list(filter(es_impar, numeros))
print("Números impares:", numeros_impares)

# Elevamos los números filtrados al cuadrado
numeros_al_cuadrado = list(map(cuadrado, numeros_impares))
print("Números impares al cuadrado:", numeros_al_cuadrado)

# Sumamos los números elevados al cuadrado
suma_total = reduce(lambda x, y: x + y, numeros_al_cuadrado)
print("Suma de los números impares al cuadrado:", suma_total)
