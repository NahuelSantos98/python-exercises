from addProduct import addProduct
from showProducts import showProducts
from findProduct import findProduct
from deleteProduct import deleteProduct

productList = []


def showMenu():
    print("\n--- MENÚ ---")
    print("1. Agregar productos")
    print("2. Mostrar productos cargados")
    print("3. Buscar un producto")
    print("4. Eliminar un producto")
    print("5. Salir")


while True:
    showMenu()
    option = int(input("Que opción quieres realizar? "))

    if option == 1:
        addProduct(productList)

    if option == 2:
        showProducts(productList)
    
    if option == 3:
        findProduct(productList)

    if option == 4:
        deleteProduct(productList)

    if option == 5 or option == "":
        print("Gracias por usar el sistema.")
        break