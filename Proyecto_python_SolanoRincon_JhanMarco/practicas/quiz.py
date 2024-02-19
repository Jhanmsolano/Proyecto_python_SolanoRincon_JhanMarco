import os



def limpiar_consola():
    # Para sistemas operativos Windows
    if os.name == 'nt':
        _ = os.system('cls')
    # Para sistemas operativos basados en Unix (Linux, macOS)
    else:
        _ = os.system('clear')



def menu():
    limpiar_consola()
    campus={
    "Sputnik": {"activity": "classes", "students access": True, "schedule": "6 am to 10 pm", "capacity": 35},

    "Artemis": {"activity": "classes", "students access": True, "schedule": "6 am to 10 pm", "capacity": 30},

    "Apollo": {"activity": "classes", "students access": True, "schedule": "6 am to 10 pm", "capacity": 30},

    "Houston": {"activity": "teachers room", "students access": False, "schedule": "when teachers need", "capacity": 6},

    "Review": {"activity": "skills review", "students access": True, "schedule": "24/7", "capacity": 100}
}

    opcion=int(input("""*****ESTAS EN EL MENU PRINCIPAL***** \n1.espacios que tiene acceso los campers  \n2.sitios de recreo cuando no hay clases \n3.donde no me puedo sentar \n4.promedio de espacios destinados a clase \n5.salir \ningrese la opcion segun corresponda: """))
    while True:
        if opcion == 1:
            print("Los siguientes sitios están disponibles para los estudiantes:")
            for lugar, detalles in campus.items():
                if detalles["students access"]:
                    print(f"- {lugar}")
            break
        
        elif opcion==2:
            print('sitios recreativos')
            for lugar,detalles in campus.items():
                if detalles["activity"]=="skills review":
                    print(f"{lugar}")
            break
        elif opcion==3:
            print("los sitios donde no puedo sentarme a estudiar como camper")
            for lugar, detalles in campus.items():
                if detalles["students access"]==False:
                    print(f"- {lugar}")
            break
            
        elif opcion==4:
            espacios_clases = [detalles["capacity"] for detalles in campus.values() if detalles["activity"] != "teachers room"]
            if espacios_clases:
                promedio = sum(espacios_clases) / len(espacios_clases)
                print(f"El promedio de espacios destinados a clases es: {round(promedio)}")
                break
            else:
                print("No hay espacios destinados a clases.")
        elif opcion == 5:
            break
        else:
            print("Opción no válida.")
            break
        
menu()