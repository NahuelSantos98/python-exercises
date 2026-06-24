# Lo pensé como para que si el dato es incorrecto, que lo vuelva a pedir.
def pedir_nombre():
    while True:
        nombre = input("¿Qué producto es? ").strip().capitalize()

        if nombre == "":
            print("Error: el nombre no puede estar vacío.")
            continue

        return nombre