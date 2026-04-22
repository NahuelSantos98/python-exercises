""" 
Ejemplo 1: Uso básico de range().
En este primer ejemplo, generamos una secuencia de números desde 0 hasta 4. 
Notá que el número de "fin" (5) no está incluido.
"""
for i in range(5):
print(i)
# 0
# 1
# 2
# 3
# 4

"""
Ejemplo 2: Valor de inicio específico.
Si queremos que el bucle comience desde un número distinto de 0, podemos indicarlo
pasando dos argumentos a range(inicio, fin).
"""
for i in range(3, 7):
print(i)
# 3
# 4
# 5
# 6

"""
Ejemplo 3: El parámetro paso.
Podemos controlar el intervalo entre cada número de la secuencia con el parámetro paso.
Esto es útil si queremos saltar números.
"""
for i in range(0, 10, 2):
print(i)
# 0
# 2
# 4
# 6
# 8

"""
Ejemplo 4: Secuencias decrecientes.
También podemos usar range() para generar secuencias decrecientes, indicando un valor
de paso negativo.
"""
for i in range(10, 0, -2):
print(i)
# 10
# 8
# 6
# 4
# 2

"""
Ejemplo 5: El uso de range() para recorrer listas
Podemos usar range() para iterar sobre los índices de una lista y acceder a sus elementos.
"""
frutas = ["manzana", "banana", "naranja"]
for i in range(len(frutas)):
print(f"Fruta {i + 1}: {frutas[i]}")
# Fruta 1: manzana
# Fruta 2: banana
# Fruta 3: naranja