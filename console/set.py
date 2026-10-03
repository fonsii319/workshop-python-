"""
SET (set)
Colección de elementos únicos y sin orden garantizado.
"""

numeros = {1, 2, 3, 3, 4, 4}

# Los duplicados desaparecen
print(numeros)

# Agregar
numeros.add(5)
print(numeros)

# Eliminar
numeros.remove(2)
print(numeros)

# Operaciones entre conjuntos
a = {1, 2, 3}
b = {3, 4, 5}

print(a | b)  # unión
print(a & b)  # intersección
print(a - b)  # diferencia

# Verificar pertenencia
print(3 in a)

# EJERCICIO:
# Crea dos sets de números y encuentra:
# unión, intersección y diferencia.
