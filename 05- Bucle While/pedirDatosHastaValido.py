nombre = ""
intentos = 0

while intentos < 3 and nombre == "":
    nombre = input("Cual es tu nombre? ")
    intentos += 1
    if nombre == "":
        print("Nombre tiene que ser valido")
    print("Intento numero: ", intentos)

print(nombre)