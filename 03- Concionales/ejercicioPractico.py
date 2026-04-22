"""
● Solicite al cliente su nombre, apellido, edad y correo
electrónico.
● Compruebe que el nombre, el apellido y el correo no estén
en blanco, y que la edad sea mayor de 18 años.
● Muestre los datos por la terminal, en el orden que se
ingresaron. Si alguno de los datos ingresados no cumple los
requisitos, sólo mostrar el texto “ERROR!”.
"""

def pedirDatos():
    nombre = input("Cual es tu nombre? ")
    if not(nombre):
        print("Nombre es obligatorio")
        return

    apellido = input("Cual es tu apellido? ")
    if not(apellido):
        print("Apellido es obligatorio")
        return
    
    edad = int(input("Cual es tu edad? "))
    if edad < 18:
        print("Tenés que ser mayor")
        return
    
    email = input("Cual es tu email? ")
    if not(email):
        print("Email es obligatorio")
        return

    print(nombre, apellido, edad, email)


pedirDatos()