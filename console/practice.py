"""
PRACTICA FINAL
Combina varios tipos de datos de Python.
"""

# Datos de un producto
nombre = "Laptop"
precio = 799.99
cantidad = 2
disponible = True
categorias = ["Tecnología", "Computadoras"]
especificaciones = {
    "marca": "Ejemplo",
    "ram": "16 GB"
}

# Cálculo
total = precio * cantidad

print("Producto:", nombre)
print("Precio:", precio)
print("Cantidad:", cantidad)
print("Disponible:", disponible)
print("Categorías:", categorias)
print("Especificaciones:", especificaciones)
print("Total:", total)

# Condición
if disponible and cantidad > 0:
    print("El producto puede comprarse.")
else:
    print("El producto no está disponible.")

# RETO:
# Crea un producto diferente utilizando:
# str, float, int, bool, list y dict.
# Calcula el total y muestra toda la información.