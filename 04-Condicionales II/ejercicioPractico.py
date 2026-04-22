"""
● Formatee correctamente los textos ingresados en “apellido”
y “nombre”, convirtiendo la primera letra de cada palabra a
mayúsculas y el resto en minúsculas.
● Asegurarse que el correo electrónico no tenga espacios y
contenga solo una “@”.
● Que clasifique a sus clientes por rango etario basándose en
su edad (“Niño/a” para los y las menores de 15 años,
“Adolescente” de 15 a 18 y “Adulto/a” para personas
mayores de 18 años.)
"""

def formateoDatos():
    nombre = input("Cual es tu nombre? ").title()
    apellido = input("Cual es tu apellido? ").title()

    edadInput = int(input("Cual es tu edad? "))
    edad = ""
    if edadInput < 15:
        edad = "Niño"
    elif edadInput < 18:
        edad = "Adolescente"
    else:
        edad = "Adulto"

    email = input("Cual es tu email? ").strip().lower()
    if email.count("@") != 1:
        print("El email debe tener una sola '@'.")
        return

    print(f'Nombre: {nombre}\nApellido: {apellido}\nEdad: {edad}\nEmail: {email}')

formateoDatos()