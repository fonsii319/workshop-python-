"""
DICTIONARY (dict)
Colección de pares clave: valor.
"""

persona = {
    "nombre": "Kevin",
    "edad": 20,
    "ciudad": "San Salvador"
}

print(persona)

# Acceder a valores
print(persona["nombre"])
print(persona["edad"])

# Agregar una clave
persona["profesion"] = "Programador"
print(persona)

# Modificar
persona["edad"] = 21
print(persona)

# Eliminar
del persona["profesion"]
print(persona)

# Recorrer claves y valores
for clave, valor in persona.items():
    print(clave, ":", valor)

# get() evita un error si la clave no existe
print(persona.get("telefono", "No registrado"))

# EJERCICIO:
# Crea un diccionario de un producto con:
# nombre, precio, cantidad y cate