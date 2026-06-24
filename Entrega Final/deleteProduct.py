def showMenuDelete():
    print("\n--- MENÚ DE ELIMINACION ---")
    print("1. Eliminar por ID")
    print("2. Eliminar por nombre")
    print("3. Volver")

def deleteById():
    try:
        idToDelete = int(
            input("¿Cuál es el ID que quiere eliminar? ")
        )

        if idToDelete < 0:
            print("ID inválido.")
            return

        archivo = open("./results/products.txt", "r")

        productos = archivo.readlines()

        archivo.close()

        productosActualizados = []
        productoEncontrado = False

        for linea in productos:
            datos = linea.strip().split(",")

            productId = int(datos[0])

            if productId == idToDelete:
                productoEncontrado = True
            else:
                productosActualizados.append(linea)

        if productoEncontrado:
            archivo = open("./results/products.txt", "w")

            archivo.writelines(productosActualizados)

            archivo.close()

            print("Producto eliminado correctamente.")
        else:
            print("Producto no encontrado.")

    except ValueError:
        print("Error: el ID debe ser un número entero.")

    except FileNotFoundError:
        print("Error: no se encontró el archivo products.txt.")


def deleteByName():
    nameToDelete = input(
        "¿Cuál es el nombre que quiere eliminar? "
    ).strip().capitalize()

    if nameToDelete == "":
        print("Nombre inválido.")
        return

    try:
        archivo = open("./results/products.txt", "r")

        productos = archivo.readlines()

        archivo.close()

        productosActualizados = []
        productoEncontrado = False

        for linea in productos:
            datos = linea.strip().split(",")

            productName = datos[1]

            if productName == nameToDelete:
                productoEncontrado = True
            else:
                productosActualizados.append(linea)

        if productoEncontrado:
            archivo = open("./results/products.txt", "w")

            archivo.writelines(productosActualizados)

            archivo.close()

            print("Producto eliminado correctamente.")
        else:
            print("Producto no encontrado.")

    except FileNotFoundError:
        print("Error: no se encontró el archivo products.txt.")


def deleteProduct():
    showMenuDelete()

    try:
        optionToDelete = int(
            input("¿Qué tipo de método quiere realizar? ")
        )

        if optionToDelete == 1:
            deleteById()

        elif optionToDelete == 2:
            deleteByName()

        elif optionToDelete == 3:
            print("Volviendo...")

        else:
            print("Opción inválida.")

    except ValueError:
        print("Error: debe ingresar una opción numérica.")