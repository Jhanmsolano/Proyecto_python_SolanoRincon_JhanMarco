import json,os,menus
datos=[]

def cargarDatos():
    menus.limpiar_consola()
    with open("rutas.json", "r") as file:
        respuesta = json.load(file)
        return respuesta

def guardarDatos(datos):
    menus.limpiar_consola()
    with open("rutas.json", "w") as file:
        escritura = json.dumps(datos, indent=4)
        file.write(escritura)

def crearRuta():
    menus.limpiar_consola
    try:
        rutas = list(cargarDatos())
        Nombres = input("Ingrese el nombre de la ruta: ")
        modulo1 = input("ingrese el modulo 1: ")
        modulo2 = input('ingrese el modulo 2: ')
        modulo3 = input('ingrese el modulo 3: ')
        
        ruta = {"Nombres": Nombres,"Modulo 1":modulo1,"Modulo 2":modulo2,"Modulo 3":modulo3}
        rutas.append(ruta)
        guardarDatos(ruta)
        print("ruta creado con éxito!")
    except Exception:
        print("Ocurrió un error al crear ruta!")

def eliminarRuta():
    menus.limpiar_consola()
    try:
        ruta = list(cargarDatos())
        for i in range(len(ruta)):
            print(str(i),"->",ruta[i])
        opc = int(input("Ingrese el indice de la ruta a borrar: "))
        ruta.pop(opc)
        guardarDatos(ruta)
        print("ruta borrada con éxito!")
    except Exception:
        print("Ocurrió un error al borrar ruta!")


def mostrarTodosLasRutas():
    menus.limpiar_consola()
    try:
        ruta = list(cargarDatos())
        for i in range(len(ruta)):
            print(str(i),"->",ruta[i])
    except Exception:
        print("Ocurrió un error al mostrar ruta!")
        


def actualizarRutas():
    menus.limpiar_consola()
    try:
        ruta = list(cargarDatos())
        if not ruta:
            print("No hay campers para actualizar.")
            return

        for i in range(len(ruta)):
            print(str(i),"->",ruta[i])

        opc = int(input("Ingrese el número de la ruta a actualizar: "))
        menus.limpiar_consola()
        if opc < 0 or opc >= len(ruta):
            print("El número ingresado está fuera de rango.")
            return

        rutas = ruta[opc]
        print("ruta seleccionado:", rutas)

        nombre = input("Ingrese el nuevo nombre de la ruta (deje vacío para mantener el actual): ")
        if nombre:
            rutas["Nombres"] = nombre

        modulo1 = input("Ingrese el nuevo modulo 1 de la ruta (deje vacío para mantener el actual): ")
        if modulo1:
            rutas["Modulo 1"] = modulo1

        modulo2 = input("Ingrese el nuevo modulo 2 de la ruta (deje vacío para mantener la actual): ")
        if modulo2:
            rutas["Modulo 2"] = modulo2
            
        modulo3 = input("ingrese el nuevo modulo 3 de la ruta (deje vacío para mantener el actual): ")
        if modulo3:
            rutas["Modulo 3"]=modulo3
            
        
        ruta[opc] = rutas
        guardarDatos(ruta)
        print("ruta actualizado con éxito!")
    except Exception as e:
        print("Ocurrió un error al actualizar el camper:", e)