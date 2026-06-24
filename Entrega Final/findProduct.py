from utils.show_product import show_product

def showMenuFind():
    print("\n--- MENÚ DE BÚSQUEDA ---")
    print("1. Buscar por ID")
    print("2. Buscar por nombre")
    print("3. Volver")


def findById():
    try:
        idToFind = int(input("¿Cuál es el ID que quiere buscar? "))

        if idToFind < 0:
            print("ID inválido.")
            return

        archivo = open("./results/products.txt", "r")

        productos = archivo.readlines()

        archivo.close()

        for linea in productos:
            datos = linea.strip().split(",")

            productId = int(datos[0])

            if productId == idToFind:
                show_product(datos)
                return

        print("Producto no encontrado.")

    except ValueError:
        print("Error: el ID debe ser un número entero.")

    except FileNotFoundError:
        print("Error: no se encontró el archivo products.txt.")


def findByName():
    nameToFind = input(
        "¿Cuál es el nombre que quiere buscar? "
    ).strip().lower()

    if nameToFind == "":
        print("Nombre inválido.")
        return

    try:
        archivo = open(
            "./results/products.txt",
            "r",
            encoding="utf-8"
        )

        productos = archivo.readlines()

        archivo.close()

        encontrado = False

        for linea in productos:
            datos = linea.strip().split(",")

            productName = datos[1].lower()

            if nameToFind in productName:
                show_product(datos)
                encontrado = True

        if not encontrado:
            print("Producto no encontrado.")

    except FileNotFoundError:
        print("Error: no se encontró el archivo products.txt.")
    nameToFind = input(
        "¿Cuál es el nombre que quiere buscar? "
    ).strip().capitalize()

    if nameToFind == "":
        print("Nombre inválido.")
        return

    try:
        archivo = open("./results/products.txt", "r")

        productos = archivo.readlines()

        archivo.close()

        for linea in productos:
            datos = linea.strip().split(",")

            productName = datos[1]

            if productName == nameToFind:
                show_product(datos)
                return

        print("Producto no encontrado.")

    except FileNotFoundError:
        print("Error: no se encontró el archivo products.txt.")


def findProduct():
    showMenuFind()

    try:
        optionFind = int(
            input("¿Qué tipo de búsqueda quiere realizar? ")
        )

        if optionFind == 1:
            findById()

        elif optionFind == 2:
            findByName()

        elif optionFind == 3:
            print("Volviendo...")

        else:
            print("Opción inválida.")

    except ValueError:
        print("Error: debe ingresar una opción numérica.")