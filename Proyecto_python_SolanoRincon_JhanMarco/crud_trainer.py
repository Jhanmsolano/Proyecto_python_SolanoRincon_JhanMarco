import json
import menus

datos = []

def cargarDatos():
    menus.limpiar_consola()
    with open("trainer.json", "r") as file:
        respuesta = json.load(file)
        return respuesta

def guardarDatos(datos):
    menus.limpiar_consola()
    with open("trainer.json", "w") as file:
        escritura = json.dumps(datos, indent=4)
        file.write(escritura)

def crearTrainer():
    menus.limpiar_consola
    try:
        trainers = list(cargarDatos())
        documento=int(input("ingrese por favor un documento"))
        for trainer in trainers:
            if trainer["Documento"] == documento:
                print("¡Este camper ya está registrado!")
                return

        Nombres = input("Ingrese sus nombres: ")
        Apellidos = input("ingrese sus apellidos: ")
        direccion = input('ingrese su direccion: ')
        telefono = int(input('ingrese un numero de telefono'))
        ruta="ninguna"
        trainer = {"Nombres": Nombres, "Apellidos": Apellidos, "Direccion": direccion,"Telefono":telefono,"Ruta":ruta,"Documento":documento}
        trainers.append(trainer)
        guardarDatos(trainers)
        print("trainer creado con éxito!")
    except Exception:
        print("Ocurrió un error al crear trainer!")
        

def eliminarTrainer():
    menus.limpiar_consola()
    try:
        trainer = list(cargarDatos())
        for i in range(len(trainer)):
            print(str(i),"->",trainer[i])
        opc = int(input("Ingrese el indice del camper a borrar: "))
        trainer.pop(opc)
        guardarDatos(trainer)
        print("trainer borrado con éxito!")
    except Exception:
        print("Ocurrió un error al borrar trainer!")


def mostrarTrainer():
    menus.limpiar_consola()
    try:
        trainer = list(cargarDatos())
        for i in range(len(trainer)):
            print(str(i),"->",trainer[i]["tipo"])
        opc = int(input("Ingrese el número del trainer a mostrar: "))
        print(trainer[opc])
    except Exception:
        print("Ocurrió un error al mostrar trainer!")

def mostrarTodosLosTrainer():
    menus.limpiar_consola()
    try:
        trainer = list(cargarDatos())
        for i in range(len(trainer)):
            print(str(i),"->",trainer[i])
    except Exception:
        print("Ocurrió un error al mostrar camper!")


def actualizarTrainerCoordinador():
    menus.limpiar_consola()
    try:
        trainer = list(cargarDatos())
        if not trainer:
            print("No hay trainers para actualizar.")
            return

        for i in range(len(trainer)):
            print(str(i),"->",trainer[i])

        opc = int(input("Ingrese el número del trainer a actualizar: "))
        menus.limpiar_consola()
        if opc < 0 or opc >= len(trainer):
            print("El número ingresado está fuera de rango.")
            return

        trainers = trainer[opc]
        print("trainer seleccionado:", trainers)

        nombre = input("Ingrese el nuevo nombre del trainer (deje vacío para mantener el actual): ")
        if nombre:
            trainers["Nombres"] = nombre

        apellidos = input("Ingrese los nuevos apellidos del trainer (deje vacío para mantener el actual): ")
        if apellidos:
            trainers["Apellidos"] = apellidos

        direccion = input("Ingrese la nueva direccion del trainer (deje vacío para mantener la actual): ")
        if direccion:
            trainer["Direccion"] = direccion
            
        telefono=int(input("ingrese el nuevo telefono del trainer (deje vacío para mantener la actual):"))
        if telefono:
            trainers["Telefono"]=telefono
            
        ruta=input("ingrese la ruta del trainer (deje vacio para mantener actual)")
        if ruta:
            trainer["Ruta"]=ruta

        trainer[opc] = trainers
        guardarDatos(trainer)
        print("trainer actualizado con éxito!")
    except Exception:
        print("Ocurrió un error al actualizar el trainer!")

def actualizarTrainer():
    menus.limpiar_consola()
    try:
        trainer = list(cargarDatos())
        if not trainer:
            print("No hay trainers para actualizar.")
            return

        for i in range(len(trainer)):
            print(str(i),"->",trainer[i])

        opc = int(input("Ingrese el número del trainer a actualizar: "))
        menus.limpiar_consola()
        if opc < 0 or opc >= len(trainer):
            print("El número ingresado está fuera de rango.")
            return

        trainers = trainer[opc]
        print("trainer seleccionado:", trainers)

        nombre = input("Ingrese el nuevo nombre del trainer (deje vacío para mantener el actual): ")
        if nombre:
            trainers["Nombres"] = nombre

        apellidos = input("Ingrese los nuevos apellidos del trainer (deje vacío para mantener el actual): ")
        if apellidos:
            trainers["Apellidos"] = apellidos

        direccion = input("Ingrese la nueva direccion del trainer (deje vacío para mantener la actual): ")
        if direccion:
            trainer["Direccion"] = direccion
            
        telefono=int(input("ingrese el nuevo telefono del trainer (deje vacío para mantener la actual):"))
        if telefono:
            trainers["Telefono"]=telefono
            
        
        trainer[opc] = trainers
        guardarDatos(trainer)
        print("trainer actualizado con éxito!")
    except Exception:
        print("Ocurrió un error al actualizar el trainer!")
        



