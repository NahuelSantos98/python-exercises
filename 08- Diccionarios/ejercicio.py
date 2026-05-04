"""
Crear un diccionario llamado productos donde las claves sean los nombres
de los productos y los valores sean sus precios.

Permitir agregar productos y sus precios hasta que se decida finalizar.

Mostrar el contenido del diccionario después de cada operación.
"""

products = {}

while True:
    productName = input("Ingrese el nombre del producto: ")
    productPrice = float(input("Ingrese el precio del producto: "))

    products[productName] = productPrice

    continueProduct = input("¿Desea agregar otro producto? (s/n): ")
    if continueProduct == "n":
        break

print(products)