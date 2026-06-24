# Lo pensé como para que si el dato es incorrecto, que lo vuelva a pedir.
def pedir_entero(mensaje, campo):
    while True:
        try:
            valor = int(input(mensaje))

            if valor < 0:
                print(f"Error: {campo} debe ser 0 o mayor.")
                continue

            return valor

        except ValueError:
            print(f"Error: {campo} debe ser un número entero.")