"""
LIST (list)
Colección ordenada y modificable de elementos.
"""

frutas = ["manzana", "banana", "naranja"]

print(frutas)

# Acceder a elementos
print(frutas[0])
print(frutas[-1])

# Modificar
frutas[1] = "pera"
print(frutas)

# Agregar
frutas.append("uva")
print(frutas)

# Insertar
frutas.insert(1, "mango")
print(frutas)

# Eliminar
frutas.remove("mango")
print(frutas)

# Cantidad de elementos
print(len(frutas))

# Recorrer una lista
for fruta in frutas:
    print(fruta)

# EJERCICIO:
# Crea una lista con 5 nombres.
# Agrega un nombre, elimina otro y recorre la lista con for.