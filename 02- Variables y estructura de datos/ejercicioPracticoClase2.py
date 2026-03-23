# Solicite al cliente su nombre, apellido, edad y correo electrónico.
# Almacene estos datos en variables.
# Los muestre organizados en forma de una tarjeta de presentación en la pantalla.

nombre = None
apellido = None
edad = None
email = None

def pedirDatos():
    global nombre, apellido, edad, email

    nombre = input("Cual es tu nombre? ")
    apellido = input("Cual es tu apellido? ")
    edad = int(input("Cuantos años tenés? "))
    email = input("Cual es tu correo electronico? ")

pedirDatos()

for i in range(3):  #Agrego un For para poder separar automatiamente lo que serían los inputs y las respuestas en la consola (No le den bola a esto).
    print("      ")

print(f'Nombre completo: {nombre} {apellido}')  #Para formatted strings se utiliza la f previo a la primer comilla y encapsular la variable en {}
print('Edad:', edad)
print('Email:', email)
