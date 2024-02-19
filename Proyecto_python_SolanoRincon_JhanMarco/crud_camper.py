import json
import menus

def cargarDatos():
    menus.limpiar_consola()
    with open("Camper.json", "r") as file:
        respuesta = json.load(file)
        return respuesta

def guardarDatos(datos):
    menus.limpiar_consola()
    with open("Camper.json", "w") as file:
        escritura = json.dumps(datos, indent=4)
        file.write(escritura)

def crearCamper():
    menus.limpiar_consola()
    try:
        campers = list(cargarDatos())
        documento = int(input("Ingrese su número de documento: "))
        for camper in campers:
            if camper["Documento"] == documento:
                print("¡Este camper ya está registrado!")
                return


        Nombres = input("Ingrese sus nombres: ")
        Apellidos = input("Ingrese sus apellidos: ")
        direccion = input('Ingrese su dirección: ')
        acudiente = input('Ingrese un acudiente: ')
        telefono = int(input('Ingrese un número de teléfono: '))
        estado = 'proceso de ingreso'
        riesgo = "ninguno"
        ruta = "ninguna"
        
        camper = {"Nombres": Nombres, "Apellidos": Apellidos, "Direccion": direccion, "Acudiente": acudiente, "Telefono": telefono, "Estado": estado, "Riesgo": riesgo, "Ruta": ruta, "Documento": documento}
        campers.append(camper)
        guardarDatos(campers)
        print("¡Camper creado con éxito!")
    except Exception as e:
        print("Ocurrió un error al crear camper:", e)

def eliminarCamper():
    menus.limpiar_consola()
    try:
        campers = list(cargarDatos())
        for i in range(len(campers)):
            print(str(i),"->",campers[i])
        opc = int(input("Ingrese el indice del camper a borrar: "))
        campers.pop(opc)
        guardarDatos(campers)
        print("Camper borrado con éxito!")
    except Exception as e:
        print("Ocurrió un error al borrar camper:", e)


def mostrarCamper():
    menus.limpiar_consola()
    try:
        camper = list(cargarDatos())
        for i in range(len(camper)):
            print(str(i),"->",camper[i]["tipo"])
        opc = int(input("Ingrese el número del camper a mostrar: "))
        print(camper[opc])
    except Exception as e:
        print("Ocurrió un error al mostrar camper:", e)

def mostrarTodosLosCampers():
    menus.limpiar_consola()
    try:
        camper = list(cargarDatos())
        for i in range(len(camper)):
            print(str(i),"->",camper[i])
    except Exception as e:
        print("Ocurrió un error al mostrar camper:", e)


def actualizarCamperCoordinador():
    menus.limpiar_consola()
    try:
        camper = list(cargarDatos())
        if not camper:
            print("No hay campers para actualizar.")
            return

        for i in range(len(camper)):
            print(str(i),"->",camper[i])

        opc = int(input("Ingrese el número del camper a actualizar: "))
        menus.limpiar_consola()
        if opc < 0 or opc >= len(camper):
            print("El número ingresado está fuera de rango.")
            return

        campers = camper[opc]
        print("camper seleccionado:", campers)

        nombre = input("Ingrese el nuevo nombre del camper (deje vacío para mantener el actual): ")
        if nombre:
            campers["Nombres"] = nombre

        apellidos = input("Ingrese los nuevos apellidos del camper (deje vacío para mantener el actual): ")
        if apellidos:
            campers["Apellidos"] = apellidos

        direccion = input("Ingrese la nueva direccion del camper (deje vacío para mantener la actual): ")
        
        if direccion:
            campers["Direccion"] = direccion
            
        acudiente = input("ingrese el nuevo apellido del camper (deje vacío para mantener el actual): ")
        if acudiente:
            campers["Acudiente"]=acudiente
            
        telefono=int(input("ingrese el nuevo telefono del camper (deje vacío para mantener el actual):"))
        if telefono:
            campers["Telefono"]=telefono
            
        estado=input("por favor ingrese el nuevo estado del camper (deje vacío para mantener el actual): ")
        if estado:
            campers["Estado"]=estado
            
        riesgo=input("ingrese le nuevo riesgo del camper (deje vacío para mantener el actual): ")
        if riesgo:
            campers["Riesgo"]=riesgo
            
        nota_practica=int(input("ingrese la nota practica del camper (deje vacío para mantener el actual): "))
        if nota_practica:
            campers["Nota practica"]=nota_practica
            
        nota_teorica=int(input("ingrese la nota teorica del camper (deje vacío para mantener el actual): "))
        if nota_teorica:
            campers["Nota teorica"]=nota_teorica

        camper[opc] = campers
        guardarDatos(camper)
        print("camper actualizado con éxito!")
    except Exception as e:
        print("Ocurrió un error al actualizar el camper:", e)

def actualizarCamper():
    menus.limpiar_consola()
    try:
        camper = list(cargarDatos())
        if not camper:
            print("No hay campers para actualizar.")
            return

        for i in range(len(camper)):
            print(str(i),"->",camper[i])
        
        opc = int(input("Ingrese el número del camper a actualizar: "))
        menus.limpiar_consola()
        if opc < 0 or opc >= len(camper):
            print("El número ingresado está fuera de rango.")
            return

        campers = camper[opc]
        print("camper seleccionado:", campers)

        nombre = input("Ingrese el nuevo nombre del camper (deje vacío para mantener el actual): ")
        if nombre:
            campers["Nombres"] = nombre

        apellidos = input("Ingrese los nuevos apellidos del camper (deje vacío para mantener el actual): ")
        if apellidos:
            campers["Apellidos"] = apellidos

        direccion = input("Ingrese la nueva direccion del camper (deje vacío para mantener la actual): ")
        if direccion:
            campers["Direccion"] = direccion
            
        acudiente = input("ingrese el nuevo apellido del camper (deje vacío para mantener el actual): ")
        if acudiente:
            campers["Acudiente"]=acudiente
            
        telefono=int(input("ingrese el nuevo telefono del camper (deje vacío para mantener el actual):"))
        if telefono:
            campers["Telefono"]=telefono
        
        documento=int(input("ingrese el numero de identificacion"))
        if documento:
            campers["Documento"]=documento
            

        camper[opc] = campers
        guardarDatos(camper)
        print("camper actualizado con éxito!")
    except Exception as e:
        print("Ocurrió un error al actualizar el camper:", e)

def ingresarNotaCamper():
    menus.limpiar_consola()
    try:
        campers = list(cargarDatos())
        
        identificacion = int(input("Por favor ingresa el número de identificación del camper: "))
        
        camper_encontrado = None
        for i in range(len(campers)):
            print(str(i),"->",campers[i]["Documento"])
            if campers[i]["Documento"] == identificacion:
                camper_encontrado = campers[i]
                break
        
        if camper_encontrado:
            
            nota_teorica = int(input("Por favor ingresa la nota teorica: "))
            nota_filtro = int(input("Por favor ingresa la nota del filtro: "))
            
            
            
            camper_encontrado["Nota teorica"] = nota_teorica
            camper_encontrado["Nota filtro"] = nota_filtro
            promedio = (nota_filtro + nota_teorica) / 2
            if promedio >= 60:
                camper_encontrado["Estado"] = "aprobado"
            else:
                camper_encontrado["Estado"] = "bajo rendimiento"
                
            guardarDatos(campers)
            print("Notas ingresadas con exito!")
        else:
            print("No se encontro ningún camper con ese número de identificacion.")
    except Exception as e:
        print("Ocurrio un error al ingresar notas:", e)
