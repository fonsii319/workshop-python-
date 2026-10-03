"""
STRING (str)
Texto en Python.
"""

nombre = "Kevin"
mensaje = 'Hola, mundo'

print(nombre)
print(mensaje)

# Concatenar textos
nombre = "Ana"
apellido = "Lopez"
nombre_completo = nombre + " " + apellido

print(nombre_completo)

# f-strings: una forma cómoda de insertar variables
edad = 20
print(f"Mi nombre es {nombre} y tengo {edad} años.")

# Índices
texto = "Python"
print(texto[0])
print(texto[1])
print(texto[-1])

# Métodos útiles
frase = "  hola python  "

print(frase.upper())
print(frase.lower())
print(frase.strip())
print(frase.replace("python", "mundo"))

# Longitud
print(len("Python"))

# EJERCICIO:
# Crea variables nombre, ciudad y profesion.
# Imprime una frase usando una f-string.

