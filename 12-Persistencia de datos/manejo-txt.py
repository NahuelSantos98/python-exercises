
# Lo habilita como para empezar a trabajar sobre ese archivo. 
# "r" para leer un archivo existente.
# "w" para escribir en un archivo (crea uno nuevo si no existe, y si existe, lo sobreescribe).
# "r+" para lectura y escritura combinadas
# "a" para agregar contenido al final de un archivo existente.

# .read() me da TODAS las lineas juntas
# archivo = open('datos.txt', 'r')
# leyendo_archivo= archivo.read() 
# print(leyendo_archivo)

# .readlines() me da linea por linea y los almacena en una lista que se puede iterar.
# archivo = open('datos.txt', 'r')
# leyendo_archivo_linea_por_linea = archivo.readlines()
# for linea in leyendo_archivo_linea_por_linea:
#     print(f"------------- {linea.strip()} ----------------")


# Sobreescribe el archivo. Borra todo lo existente y prioriza lo que pone nuevo.
# El .close() vacía el buffer y libera el archivo, asegurando que todo lo escrito quede guardado en disco.
# archivo = open('datos.txt', 'w')
# modificando_archivo = archivo.write('Yo bien, \ny vos?\n')
# segunda_modificacion = archivo.write('mal\n')
# archivo.close()

# archivo_lectura = open('datos.txt', 'r')
# leyendo_archivo_linea_por_linea = archivo_lectura.readlines()
# for linea in leyendo_archivo_linea_por_linea:
#     print(f"------------- {linea.strip()} ----------------")

# 'a' agrega lo que escribamos al archivo en la ultima posición.
# archivo = open("datos.txt", "a")
# archivo.write("\nCuarta línea del archivo.")
# archivo.close()

# archivo_lectura = open('datos.txt', 'r')
# leyendo_archivo_linea_por_linea = archivo_lectura.readlines()
# for linea in leyendo_archivo_linea_por_linea:
#     print(f"------------- {linea.strip()} ----------------")

archivo = open('nombres.txt', 'w')
lista_nombres = ['Nahuel', 'Martin', 'Santos']

for index, nombre in enumerate(lista_nombres, start=1):
    archivo.write(f"{nombre} - {index}\n")

archivo.close()

archivo_lectura = open('nombres.txt', 'r')
nombres_lineas = archivo_lectura.readlines()

for linea in nombres_lineas:
    print(linea.strip())

archivo_lectura.close()