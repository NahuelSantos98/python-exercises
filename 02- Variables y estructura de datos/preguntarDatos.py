# Para declarar variables fuera de una function y sin valor se le tiene que asignar un valor None, 
# luego para asignarles un valor DENTRO de la function hay que importarlas con global nombreVariable 
# y ahí se pueden usar dentro de la function.

nombre = None   #Utilizamos None para asignarle un valor y que se declare bien
edad = None
altura = None
es_estudiante = None


def pedirDatosAlCliente():
    global nombre, edad, altura, es_estudiante   #La importamos a la función para que pueda serle asignado un valor definido


    nombre = input("Como te llamas? ")   #Definimos que el valor del input va a ser el valor que va a tener la variable nombre.
    edad = int(input("Cuantos años tenés? "))    #Uso de int() para que se pueda tratar como un número entero.
    altura = float(input("Cual es tu altura? "))     #Uso de float() para que luego se comporte como un tipo de dato float.
    question = input("Estudías? (si/no) ").lower()   #Uso de .lower() para que no sea caseSensitive al momento de usar el ternario.
    if question == "si" :
        es_estudiante = True
    else: es_estudiante = False


pedirDatosAlCliente()    #Ejecuta la function


print("Nombre:", nombre)
print("Edad:", edad)
print("Altura:", altura)
print("¿Es estudiante?:", es_estudiante)

print("El dato edad es de tipo: ", type(edad))
print("El dato altura es de tipo: ", type(altura))
