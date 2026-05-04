def addProduct(productList):
    productId = int(input("Cual es el id del producto? "))
    name = input("Que producto es? ").capitalize().strip()
    price = int(input("Cual es el precio? "))
    stock = int(input("Cuanto stock hay del producto? "))

    if productId < 0:
        print("Error, id invalido. Debe ser 0 o mayor.")
    
    if name == "" or len(name) <= 0:
        print("Error, nombre invalido.")
    
    if price < 0:
        print("Error, precio invalido. Debe ser 0 o mayor.")
        
    if stock < 0:
        print("Error, stock invalido. Debe ser 0 o mayor.")


    productToAdd = {
    "id": productId,
    "name": name,
    "price": price,
    "stock": stock
    }

    productList.append(productToAdd)