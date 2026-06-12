
try:
# Intentamos abrir un archivo para lectura
    archivo = open("datos.txt", "r")
# Leemos todo el contenido del archivo
    contenido = archivo.read()
    print("Contenido del archivo:")
# Mostramos el contenido del archivo
    print(contenido)
# Cerramos el archivo
    archivo.close()
# La excepción:
except FileNotFoundError:
    print("Error: El archivo 'datos.txt' no existe.")
    print("Verificá el nombre o la ubicación del archivo.")


print("=== Calculadora de División ===")
try:
    numerador = float(input("Ingresá el numerador: "))
    denominador = float(input("Ingresá el denominador: "))
# Intentamos realizar la división
    resultado = numerador / denominador
    print(f"El resultado de la división es: {resultado:.2f}")
except ValueError:
# Manejo de error si el usuario ingresa algo que no es
# un número
    print("[ERROR] Debés ingresar valores numéricos válidos.")
except ZeroDivisionError:
# Manejo de error si el usuario intenta dividir por cero
    print("[ERROR] El denominador no puede ser cero.")
    print(" Intentá nuevamente.")
    print("Gracias por usar la calculadora.")