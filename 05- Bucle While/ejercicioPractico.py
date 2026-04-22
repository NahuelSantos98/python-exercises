valorIngresos = []
meses = 0


while meses < 6 :
    valorMes = int(input("Cuanto cobró este mes? "))

# Al usar el continue, saltea el valor y no lo suma, tampoco se ejecuta el meses += 1.
# Se vuelve al inicio del bucle, por lo que no ejecuta lo que sigue.
    if valorMes < 0:
        print("El valor ha sido negativo, complete bien los datos.")
        continue
    
    valorIngresos.append(valorMes)
    meses += 1

# NO PUEDO CAMBIAR EL VALOR DE UNA VARIABLE QUE ESTA CON SCOPE GLOBAL DENTRO DE UNA FUNCTION
def sumaImporteTotal():
    importeTotal = 0
    for valor in valorIngresos:
        importeTotal += valor
    print("El importe total de los meses fue: ", importeTotal)

sumaImporteTotal()


print("El valor de los ingresos fue de: ",valorIngresos)