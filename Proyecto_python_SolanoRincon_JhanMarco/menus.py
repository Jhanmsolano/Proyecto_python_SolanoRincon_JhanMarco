import os
import crud_camper
import crud_trainer
import crud_rutas
import funciones_reporte

def limpiar_consola():
    # Para sistemas operativos Windows
    if os.name == 'nt':
        _ = os.system('cls')
    # Para sistemas operativos basados en Unix (Linux, macOS)
    else:
        _ = os.system('clear')

def menu_camper_coordinador():
    limpiar_consola()
    while True:
        opcion = int(input(''' 
1. Registrar camper 
2. Actualizar camper 
3. Eliminar camper 
4. Ingresar notas 
5. Salir 
Ingrese la opción correspondiente: '''))
        
        if opcion == 1:
            crud_camper.crearCamper()
            break
        elif opcion == 2:
            crud_camper.actualizarCamperCoordinador()
            break
        elif opcion == 3:
            crud_camper.eliminarCamper()
            break
        elif opcion == 4:
            crud_camper.ingresarNotaCamper()
            break
        elif opcion == 5:
            if confirmacion_salir():
                break
        else:
            print('Por favor, ingrese una opción válida')

def menu_camper():
    limpiar_consola()
    while True:
        opcion = int(input('''****** HAS INGRESADO AL MENÚ DEL CAMPER ***** 

1. Registrar camper 
2. Actualizar camper  
3. Salir 
Ingrese la opción correspondiente: '''))
    
        if opcion == 1:
            crud_camper.crearCamper()
            break
        elif opcion == 2:
            crud_camper.actualizarCamper()
            break
        elif opcion == 3:
            if confirmacion_salir():
                break
        else:
            print('Por favor, ingrese una opción válida')

def menu_trainer():
    limpiar_consola()
    while True:
        opcion = int(input('''******** HAS INGRESADO AL MENÚ TRAINER ******* 

1. Registrar trainer 
2. Actualizar trainer  
3. Salir 
Ingrese la opción correspondiente: '''))
    
        if opcion == 1:
            crud_trainer.crearTrainer()
            break
        elif opcion == 2:
            crud_trainer.actualizarTrainer()
            break
        elif opcion == 3:
            if confirmacion_salir():
                break
        else:
            print('Por favor, ingrese una opción válida')

def menu_trainer_coordinador():
    limpiar_consola()
    while True:
        opcion = int(input(''' 
1. Registrar trainer 
2. Actualizar trainer 
3. Eliminar trainer 
4. Salir 
Ingrese la opción correspondiente: '''))
    
        if opcion == 1:
            crud_trainer.crearTrainer()
        elif opcion == 2:
            crud_trainer.actualizarTrainerCoordinador()
        elif opcion == 3:
            crud_trainer.eliminarTrainer()
        elif opcion == 4:
            if confirmacion_salir():
                break
        else:
            print('Por favor, ingrese una opción válida')

def menu_coordinador():
    limpiar_consola()
    while True:
        opcion = int(input('''******* HAS INGRESADO AL MENÚ COORDINADOR *****

0.Ingresar al menu rutas
1. Ingresar al menú camper 
2. Ingresar al menú trainer 
3. Reportes 
4. Salir
Ingrese la opción correspondiente: '''))
        
        if opcion==0:
            menu_rutas()
            
        if opcion == 1:
            print('Has ingresado al menú del camper')
            menu_camper_coordinador()
            
        elif opcion == 2:
            print('Has ingresado al menú del trainer')
            menu_trainer_coordinador()
        elif opcion == 3:
            menu_reporte()
        elif opcion == 4:
            if confirmacion_salir():
                break
        else:
            print('Por favor, ingrese una opción válida')

def menu_principal():
    limpiar_consola()
    while True:
        opcion = int(input("""***** ESTÁS EN EL MENÚ PRINCIPAL ***** 

1. Ingresar al menú camper 
2. Ingresar al menú trainer 
3. Ingresar al menú coordinador 
4. Salir 
Ingrese la opción correspondiente: """))
        
        if opcion == 1:
            print('Has ingresado al menú del camper')
            menu_camper()
        elif opcion == 2:
            print('Has ingresado al menú del trainer')
            menu_trainer()
        elif opcion == 3:
            while True:
                contraseña = 12345
                ingreso = int(input("Por favor, ingrese su contraseña: "))
                if ingreso == contraseña:
                    print('Has ingresado al menú coordinador')
                    menu_coordinador()
                    break
                else:
                    print("Su contraseña es incorrecta")
        elif opcion == 4:
            if confirmacion_salir():
                break
        else:
            print('Por favor, ingrese una opción válida')

def confirmacion_salir():
    validacion = input("¿Realmente desea salir? Ingrese 'si' para confirmar, o cualquier otra tecla para continuar: ")
    return validacion.lower() == "si"

def menu_reporte():
    limpiar_consola()
    while True:
        opcion = int(input("""***** MENÚ REPORTES ***** 

1. Listar los campers que se encuentren en estado de inscrito. 
2. Listar los campers que aprobaron el examen inicial. 
3. Listar los entrenadores que se encuentran trabajando con CampusLands. 
4. Listar los campers que cuentan con bajo rendimiento. 
5. Listar los campers y trainers que se encuentren asociados a una ruta de entrenamiento. 
6. Mostrar cuantos campers perdieron y aprobaron cada uno de los módulos teniendo en cuenta la ruta de entrenamiento y el entrenador encargado. 
7. Salir 
INGRESE LA OPCIÓN CORRESPONDIENTE: """))
        
        if opcion == 1:
            funciones_reporte.estadoIncrito()
            break
        elif opcion == 2:
            funciones_reporte.estadoAprobado()
            break
        elif opcion == 3:
            crud_trainer.mostrarTodosLosTrainer()
            break
        elif opcion == 4:
            funciones_reporte.riesgo()
            break
        elif opcion == 5:
            print("esta opcion no funciona")
            break
        elif opcion == 6:
            print("esta opcion no  funciona")
            break
        elif opcion == 7:
            if confirmacion_salir():
                break
        else:
            print("Por favor, ingrese una opción válida")
            break

def menu_rutas():
    limpiar_consola()
    while True:
        opcion = int(input("""***** MENÚ RUTAS ***** 

1. crea ruta
2. eliminar ruta 
3. actualizar ruta
4. mostrar todas las rutas
5. Salir 
INGRESE LA OPCIÓN CORRESPONDIENTE: """))
        
        if opcion == 1:
            crud_rutas.crearRuta()
            break
        elif opcion == 2:
            crud_rutas.eliminarRuta()
            break
        elif opcion == 3:
            crud_rutas.actualizarRutas()
            break
        elif opcion == 4:
            crud_rutas.mostrarTodosLasRutas()
            break
        elif opcion == 5:
            if confirmacion_salir():
                break
        else:
            print("Por favor, ingrese una opción válida")
            break
