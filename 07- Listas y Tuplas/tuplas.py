"""
Entre Tuplas y Listas, ambas estructuras permiten almacenar múltiples valores, acceder a ellos mediante índices
y ser recorridas con bucles, pero la elección entre listas y tuplas depende del contexto. Si
necesitás manipular los datos, una lista es la mejor opción. Si buscás garantizar que los
datos permanezcan inalterados, una tupla será más adecuada.
Las tuplas son estructuras de datos similares a las listas, pero con una característica
principal que las diferencia: son inmutables. Esto significa que, una vez creada, una tupla no se puede modificar. 
No podés agregar, eliminar ni cambiar los elementos que contiene.
"""

"""
Las tuplas se definen utilizando paréntesis ( ), aunque también se pueden crear sin
paréntesis explícitos, separando los elementos por comas.
"""
# Creación de una tupla
mi_tupla = (10, 20, 30)
# Creación sin paréntesis
otra_tupla = 40, 50, 60
# Tupla con un solo elemento (requiere una coma final)
tupla_unica = (100,)

# Acceso a elementos
colores = ("rojo", "verde", "azul")
print(colores[0]) # Salida: rojo
print(colores[-1]) # Salida: azul

# Metodos:

# Cuenta cuantos valores hay con el parametro.
numeros = (1, 2, 2, 3)
print(numeros.count(2)) # Salida: 2

# Muestra el index en el que se encuentra el parametro.
frutas = ("manzana", "pera", "manzana")
print(frutas.index("pera")) # Salida: 1


# Conversiones:

#lista a tupla
mi_lista = [1, 2, 3]
mi_tupla = tuple(mi_lista)
print(mi_tupla) # Salida: (1, 2, 3)

#tupla a lista
otra_tupla = (4, 5, 6)
otra_lista = list(otra_tupla)
print(otra_lista) # Salida: [4, 5, 6]

