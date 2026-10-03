"""
NONE (NoneType)
Representa la ausencia de un valor.
"""

resultado = None

print(resultado)
print(type(resultado))

# None no es lo mismo que 0, False o ""
valor = None

if valor is None:
    print("No existe un valor todavía.")

# Ejemplo típico: una variable que recibirá información después
usuario_actual = None

# Más adelante podría recibir un valor
usuario_actual = "Kevin"

print(usuario_actual)

# Para comprobar None se recomienda usar "is"
print(usuario_actual is None)

# EJERCICIO:
# Crea una variable llamada respuesta con None.
# Comprueba si su valor es None