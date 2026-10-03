"""
BOOLEAN (bool)
Aprende desde cero a trabajar con valores True y False.
"""

# 1. Crear valores booleanos
es_mayor_de_edad = True
tiene_dinero = False

print(es_mayor_de_edad)
print(tiene_dinero)

# 2. Comparaciones: producen True o False
edad = 20
print(edad >= 18)
print(edad == 20)
print(edad != 15)

# 3. Operadores lógicos
puede_entrar = edad >= 18 and tiene_dinero
print(puede_entrar)

# 4. Negación
print(not tiene_dinero)

# 5. Verificar el tipo de dato
print(type(es_mayor_de_edad))

# EJERCICIO:
# Crea dos variables llamadas tiene_licencia y es_mayor_de_edad.
# Haz una condición que indique si una persona puede conducir.

tiene_licencia = True
es_mayor_de_edad = True

if tiene_licencia and es_mayor_de_edad:
    print("La persona puede conducir.")
else:
    print("La persona no puede conducir.")

    