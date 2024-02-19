import json,crud_camper,crud_trainer,menus



def estadoIncrito():
    menus.limpiar_consola()
    campers = crud_camper.cargarDatos()
    
    inscritos = [camper for camper in campers if camper["Estado"] == "inscrito"]
    
    if not inscritos:
        print("No hay campers en estado inscrito.")
    else:
        print("Estos campers están inscritos:")
        for i, camper in enumerate(inscritos):
            print(f"{i} -> {camper['Nombres']} {camper['Apellidos']} {camper['Estado']}")


            
            
def estadoAprobado():
    menus.limpiar_consola()
    campers = crud_camper.cargarDatos()
    
    campers_aprobados = [camper for camper in campers if camper["Estado"] == "aprobado"]
    
    if not campers_aprobados:
        print("No hay campers en estado aprobado.")
    else:
        print("Estos campers están aprobados:")
        for i, camper in enumerate(campers_aprobados):
            print(f"{i} -> {camper['Nombres']} {camper['Apellidos']} {camper['Estado']}")



def riesgo():
    menus.limpiar_consola()
    campers = crud_camper.cargarDatos()
    
    campers_en_riesgo = [camper for camper in campers if camper["riesgo"] == "bajo rendimiento"]
    
    if not campers_en_riesgo:
        print("No hay campers en riesgo de bajo rendimiento.")
    else:
        print("Estos campers están en bajo rendimiento:")
        for i, camper in enumerate(campers_en_riesgo):
            print(f"{i} -> {camper['Nombres']} {camper['Apellidos']} {camper['riesgo']}")
