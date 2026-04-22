"""
Crear una lista con los nombres de los y las clientes que
vamos a procesar. Recorrer la lista y mostrar el nombre de
cada cliente o clienta, junto con su posición en la lista (por
ejemplo, Cliente 1, Cliente 2, etc.).
2. Recorrer la lista con un for y mostrar el nombre de cada
cliente junto con su posición en la lista (por ejemplo: Cliente
1: Ana).
3. Si encuentras un nombre vacío, mostrar un mensaje de
alerta indicando que ese dato no es válido.
"""

nombresList = ["Nahuel", "Martin", "", "Santos"]

def verificacionNombres():
    for i in range(len(nombresList)):
        if nombresList[i].strip() != "":
            nombre_formateado = nombresList[i].title()
            print(f"Cliente {i + 1}: {nombre_formateado}")
        else:
            print(f"Dato en el index {i + 1} no es válido.")

verificacionNombres()