"""
Necesitamos implementar un registro ordenado de los nombres de las
empresas que trabajan con TalentoLab . Tu tarea hoy consistirá en
crear una lista, ordenada alfabéticamente, de todas ellas. Más tarde te
daré todos los detalles necesarios.
"""

empresasList = []

print("Para finalizar la creación de lista, ponga 0.")
print("Para eliminar el ultimo registro de la lista ponga 1.")

while True:
    pregunta = input("Cual es el nombre de la empresa? ").strip().lower()

    if pregunta == "0":
        break

    if pregunta == "1":
        removeEmpresa = input("Que empresa desea eliminar? ").strip().lower()
        if removeEmpresa in empresasList:
            empresasList.remove(removeEmpresa)
        else:
            print("La empresa no está en la lista.")
        continue #Evita agregar el 1 a la lista de empresas

    empresasList.append(pregunta)

empresasList.sort()

for empresa in empresasList:
    print(f"Empresa: {empresa}")