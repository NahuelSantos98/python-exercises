def showProducts():
    try:
        open("./results/products.txt", "r")

        productos = archivo.readlines()

        archivo.close()

        print("\nPRODUCTOS CARGADOS")

        if len(productos) == 0:
            print("No hay productos cargados.")
            return

        for i, linea in enumerate(productos):
            datos = linea.strip().split(",")

            productId = datos[0]
            name = datos[1]
            price = datos[2]
            stock = datos[3]

            print(f"\nProducto {i + 1}")
            print(f"ID: {productId}")
            print(f"Nombre: {name}")
            print(f"Precio: ${price}")
            print(f"Stock: {stock}")

    except FileNotFoundError:
        print("Error: no se encontró el archivo products.txt.")