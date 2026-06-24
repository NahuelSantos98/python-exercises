from addProduct import addProduct
from showProducts import showProducts
from findProduct import findProduct
from deleteProduct import deleteProduct


def showMenu():
    print("\n--- MENÚ ---")
    print("1. Agregar productos")
    print("2. Mostrar productos cargados")
    print("3. Buscar un producto")
    print("4. Eliminar un producto")
    print("5. Salir")


while True:
    showMenu()

    try:
        option = int(input("¿Qué opción quiere realizar? "))

        if option == 1:
            addProduct()

        elif option == 2:
            showProducts()

        elif option == 3:
            findProduct()

        elif option == 4:
            deleteProduct()

        elif option == 5:
            print("Gracias por usar el sistema.")
            break

        else:
            print("Opción inválida.")

    except ValueError:
        print("Error: debe ingresar una opción numérica.")