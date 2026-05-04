def showMenuFind():
    print("\n--- MENÚ DE BUSQUEDA ---")
    print("1. Buscar por ID")
    print("2. Buscar por nombre")
    print("3. Volver")


def findById(productList):
    idToFind = int(input("Cual es el id que quiere buscar? "))

    if idToFind < 0:
        print("ID inválido")
        return

    for product in productList:
        if product["id"] == idToFind:
            print(product)
            return

    print("Producto no encontrado")
    return

def findByName(productList):
    nameToFind = input("Cual es el nombre que quiere buscar? ").strip().capitalize()

    if nameToFind == "":
        print("Nombre inválido")
        return

    for product in productList:
        if product["name"] == nameToFind:
            print(product)
            return

    print("Producto no encontrado")
    return

def findProduct(productList):
    showMenuFind()
    optionFind = int(input("Que tipo de busqueda quiere realizar? "))

    if optionFind == 1:
        findById(productList)
            
    if optionFind == 2:
        findByName(productList)

    if optionFind == 3 or optionFind == "":
        print("Volviendo...")
        return