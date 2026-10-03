
"""
EJERCICIO: BOOLEAN (bool)

Objetivo:
- Pedir el nombre y la edad por consola.
- Determinar si la persona es menor de edad.
- Comprobar si la edad es exactamente 18.
"""

# Pedir datos al usuario
nombre = input("¿Cuál es tu nombre? ")
edad = int(input("¿Cuántos años tienes? "))

# Comprobar si es menor de edad
if edad < 18:
    print(f"{nombre}, eres menor de edad.")
else:
    print(f"{nombre}, eres mayor de edad.")

# Comprobar si la edad es exactamente 18
es_igual_a_18 = edad == 18

print(f"¿La edad es igual a 18? {es_igual_a_18}")

# Segundo mensaje utilizando directamente la comparación
print(f"Resultado booleano: {edad == 18}")
