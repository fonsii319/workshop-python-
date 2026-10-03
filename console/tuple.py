"""
TUPLE (tuple)
Colección ordenada que no se puede modificar después de crearla.
"""

coordenadas = (10, 20)
colores = ("rojo", "verde", "azul")

print(coordenadas)
print(colores)

# Acceder a elementos
print(colores[0])
print(colores[-1])

# Cantidad
print(len(colores))

# Desempaquetar
x, y = coordenadas
print(x)
print(y)

# Una tupla no permite:
# coordenadas[0] = 50
# Esto produciría un error.

# EJERCICIO:
# Crea una tupla con los días de la semana.
# Imprime el primer y último elemento.
