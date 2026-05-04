from findProduct import showMenuFind

def deleteById(productList):
    idToDelete = int(input("Cual es el id que quiere eliminar? "))

    if idToDelete < 0:
        print("ID inválido")
        return

    for i, product in enumerate(productList):
        if product["id"] == idToDelete:
            productList.pop(i)
            print("Producto eliminado")
            return

    print("Producto no encontrado")
    return

def deleteByName(productList):
    nameToDelete = input("Cual es el nombre que quiere eliminar? ").strip().capitalize()

    if nameToDelete == "":
        print("Nombre inválido")
        return

    for i, product in enumerate(productList):
        if product["name"] == nameToDelete:
            productList.pop(i)
            print("Producto eliminado")
            return

    print("Producto no encontrado")
    return


def deleteProduct(productList):
    showMenuFind()

    optionToDelete = int(input("Que tipo de busqueda quiere realizar? "))

    if optionToDelete == 1:
        deleteById(productList)
            
    if optionToDelete == 2:
        deleteByName(productList)

    if optionToDelete == 3 or optionToDelete == "":
        print("Volviendo...")
        return