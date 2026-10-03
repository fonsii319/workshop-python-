"""
CONVERSIÓN DE TIPOS
Aprende a convertir datos de un tipo a otro.
"""

# String a integer
numero_texto = "25"
numero = int(numero_texto)

print(numero)
print(type(numero))

# String a float
precio_texto = "19.99"
precio = float(precio_texto)

print(precio)
print(type(precio))

# Número a string
edad = 20
edad_texto = str(edad)

print(edad_texto)
print(type(edad_texto))

# Número a boolean
print(bool(1))
print(bool(0))

# String a boolean: cuidado
print(bool("False"))  # True porque el texto no está vacío.

# Lista, tupla y set
lista = [1, 2, 3]
tupla = tuple(lista)
conjunto = set(lista)

print(tupla)
print(conjunto)

# EJERCICIO:
# Convierte "100" a int, 25 a string y [1, 2, 2, 3] a set.
