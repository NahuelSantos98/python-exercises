"""Necesitamos crear una lista con los nombres de los clientes que vamos
a procesar. Además, es necesario detectar si alguno de los nombres
está en blanco y mostrar una alerta en esos casos. Luego, para los
nombres válidos, nos aseguraremos que uno comience con una letra
mayúscula y el resto en minúsculas."""

nombresList = ["Nahuel", "martiN", "", "Miguel"]

def verificacionNombres():
    for index, nombre in enumerate(nombresList):
        if nombre.strip() != "":
            nombre_formateado = nombre.title()
            print(nombre_formateado)
        else:
            print(f"Nombre en el espacio {index + 1} vacío.")

# verificacionNombres()

def verificacionNombres2():
    for index, nombre in enumerate(nombresList):
        if nombre == "":
            print(f"Nombre en index: {index + 1} vacío.")
            break
        else:
            print(f"Nombre: {nombre.title()}.")

# verificacionNombres2()

# Trabaja con el index, no con el valor
def verificacionNombres3():
    for i in range(len(nombresList)):
        if nombresList[i].strip() != "":
            nombre_formateado = nombresList[i].title()
            print(nombre_formateado)
        else:
            print(f"Nombre en el espacio {i + 1} vacío.")

# verificacionNombres3()

def iterarString():
    nombre = "Nahuel"
    for letra in nombre:
        letraFormateada = letra.upper()
        print(letraFormateada)

# iterarString()

productos = ["P01", "P02", "P03", "P04"]

def findProduct():
    request = input("Cual es el producto a buscar? ")
    
    for producto in productos:
        if producto == request.strip():
            print(producto)
            break
        print("Buscando...")
    print("Fin de la busqueda.")

# findProduct()

