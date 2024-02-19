
import json
datos = []

def cargarDatos():
    with open("veterinariBD.json", "r") as file:
        respuesta = json.load(file)
        return respuesta

def guardarDatos(datos):
    with open("veterinariBD.json", "w") as file:
        escritura = json.dumps(datos, indent=4)
        file.write(escritura)

def crearAnimal():
    try:
        animales = list(cargarDatos())
        tipo = input("Ingrese el tipo de animal: ")
        nPatas = int(input("Ingrese el numero de patas del animal: "))
        raza = input("Ingrese la raza del animal: ")
        animal = {"tipo": tipo, "nPatas": nPatas, "Raza": raza}
        animales.append(animal)
        guardarDatos(animales)
        print("Animal creado con éxito!")
    except Exception:
        print("Ocurrió un error al crear animal!")

def eliminarAnimal():
    try:
        animales = list(cargarDatos())
        for i in range(len(animales)):
            print(str(i),"->",animales[i])
        opc = int(input("Ingrese el número del animal a borrar: "))
        animales.pop(opc)
        guardarDatos(animales)
        print("Animal borrado con éxito!")
    except Exception:
        print("Ocurrió un error al borrar animal!")


def mostrarAnimal():
    try:
        animales = list(cargarDatos())
        for i in range(len(animales)):
            print(str(i),"->",animales[i]["tipo"])
        opc = int(input("Ingrese el número del animal a mostrar: "))
        print(animales[opc])
    except Exception:
        print("Ocurrió un error al mostrar animal!")

def mostrarTodosLosAnimales():
    try:
        animales = list(cargarDatos())
        for i in range(len(animales)):
            print(str(i),"->",animales[i])
    except Exception:
        print("Ocurrió un error al mostrar animal!")


def actualizarAnimal():
    try:
        animales = list(cargarDatos())
        if not animales:
            print("No hay animales para actualizar.")
            return

        for i in range(len(animales)):
            print(str(i),"->",animales[i])

        opc = int(input("Ingrese el número del animal a actualizar: "))
        if opc < 0 or opc >= len(animales):
            print("El número ingresado está fuera de rango.")
            return

        animal = animales[opc]
        print("Animal seleccionado:", animal)

        tipo = input("Ingrese el nuevo tipo de animal (deje vacío para mantener el actual): ")
        if tipo:
            animal["tipo"] = tipo

        nPatas = input("Ingrese el nuevo número de patas del animal (deje vacío para mantener el actual): ")
        if nPatas:
            animal["nPatas"] = int(nPatas)

        raza = input("Ingrese la nueva raza del animal (deje vacío para mantener la actual): ")
        if raza:
            animal["Raza"] = raza

        animales[opc] = animal
        guardarDatos(animales)
        print("Animal actualizado con éxito!")
    except Exception:
        print("Ocurrió un error al actualizar el animal!")

def actualizarAnimal():
    try:
        animales = list(cargarDatos())
        if not animales:
            print("No hay animales para actualizar.")
            return

        for i in range(len(animales)):
            print(str(i),"->",animales[i])

        opc = int(input("Ingrese el número del animal a actualizar: "))
        if opc < 0 or opc >= len(animales):
            print("El número ingresado está fuera de rango.")
            return

        animal = animales[opc]
        print("Animal seleccionado:", animal)

        tipo = input("Ingrese el nuevo tipo de animal (deje vacío para mantener el actual): ")
        if tipo:
            animal["tipo"] = tipo

        nPatas = input("Ingrese el nuevo número de patas del animal (deje vacío para mantener el actual): ")
        if nPatas:
            animal["nPatas"] = int(nPatas)

        raza = input("Ingrese la nueva raza del animal (deje vacío para mantener la actual): ")
        if raza:
            animal["Raza"] = raza

        animales[opc] = animal
        guardarDatos(animales)
        print("Animal actualizado con éxito!")
    except Exception:
        print("Ocurrió un error al actualizar el animal!")


crearAnimal()