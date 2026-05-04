def showProducts(productList):

    print("Productos cargados:")
    if len(productList) == 0:
        print("No hay productos cargados")
        return
    
    for i in range(len(productList)):
        print(f"Producto {i + 1}: {productList[i]}")

    return