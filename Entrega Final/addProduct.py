from utils.pedir_entero import pedir_entero
from utils.pedir_nombre import pedir_nombre


def addProduct():
    try:
        productId = pedir_entero(
            "¿Cuál es el ID del producto? ",
            "el ID"
        )

        name = pedir_nombre()

        price = pedir_entero(
            "¿Cuál es el precio? ",
            "el precio"
        )

        stock = pedir_entero(
            "¿Cuánto stock hay del producto? ",
            "el stock"
        )

        archivo = open("./results/products.txt", "a")

        archivo.write(
            f"{productId},{name},{price},{stock}\n"
        )

        archivo.close()

        print("Producto agregado correctamente.")

    except FileNotFoundError:
        print("Error: no se encontró la carpeta results.")
        print("Verificá la ubicación './results/products.txt'.")