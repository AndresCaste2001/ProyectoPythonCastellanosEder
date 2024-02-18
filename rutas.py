import jsonCRUD
def creacionRuta():
    listaRutas = jsonCRUD.cargarDatos("rutas.json")
    while True:
        print("*********************************************")
        print("Bienvenido a la seccion de creacion de rutas")
        print("*********************************************\n\n")
        fundamentos = []
        programacionWeb = []
        progFormal = []
        basesDatos = []
        backend = []
        try:
            nombre = input("Ingrese el nombre de la ruta: ")
            print("Ingrese tecnologias a usar en fundamentos de programacion \nIngresa 0 para finalizar..")
            while True:
                tecnologia = input()
                if tecnologia == "0":
                    break
                else:
                    fundamentos.append(tecnologia)
            print("Ingrese tecnologias a usar en programacion web: \nIngresa 0 para finalizar..")
            while True:
                tecnologia = input()
                if tecnologia == "0":
                    break
                else:
                    programacionWeb.append(tecnologia)
            print("Ingrese tecnologias a usar en programacion formal: \nIngresa 0 para finalizar..")
            while True:
                tecnologia = input()
                if tecnologia == "0":
                    break
                else:
                    progFormal.append(tecnologia)
            print("Ingrese tecnologias a usar en Bases de datos: \nIngresa 0 para finalizar..")
            while True:
                tecnologia = input()
                if tecnologia == "0":
                    break
                else:
                    basesDatos.append(tecnologia)
            print("Ingrese tecnologias a usar en backend: \nIngresa 0 para finalizar..")
            while True:
                tecnologia = input()
                if tecnologia == "0":
                    break
                else:
                    backend.append(tecnologia)
            break
        except ValueError:
            print("\nERROR: Por favor ingrese un valor valido.")
            
    listaRutas.append({'nombre':nombre,'fundamentos':fundamentos, 'programacionWeb':programacionWeb, 'progFormal':progFormal, 'basesDatos':basesDatos,'backend':backend})
    jsonCRUD.guardarDatos(listaRutas,"rutas.json")
    
def asignarRuta():
    listaAreas = jsonCRUD.cargarDatos("areaEntrenamiento.json")
    listaRutas = jsonCRUD.cargarDatos("rutas.json")
    listaTrainers = jsonCRUD.cargarDatos("trainer.json")

    print("--- Areas sin Ruta ---" )
    for index, areas in enumerate(listaAreas):
        nombre = areas.get('nombre','area sin nombre')
        ruta = areas.get('ruta','no existe la ruta')
        if ruta == "":
            print(f"{index+1} - {nombre}")

    opcion = int(input("Ingrese el indice del area que desea asignarle una ruta: "))
    

    print("--- Lista de Rutas ---")
    for index, ruta in enumerate(listaRutas):
        opcRuta = ruta.get('nombre','sin nombre')
        print(f"{index+1} - {opcRuta}")
    opcion2 = int(input("Ingrese el indice de la ruta que desea seleccionar: "))
    if listaTrainers:
        print("--- Lista de trainers ---")
        for index, trainer in enumerate(listaTrainers):
            nombreTrainer = trainer.get('nombre','sin nombre')
            print(f"{index+1} - {nombreTrainer}")
        opcion3 = int(input("Ingrese el indice del trainer: "))

        fechaInicio = input("Ingresa la fecha de inicio del curso: \nDD/MM/AAAA\n")
        fechaFinalizacion = input("Ingresa la fecha de finalizacion del curso: \nDD/MM/AAAA\n")

        trainer = listaTrainers[opcion3-1]['nombre']
        horarioArea = listaAreas[opcion-1]['horario']
        disponible = True

        for area in listaAreas:
            profe = area.get('trainer','trainer no asignado')
            horarioClase = area.get('horario','sin horario asignado')
            if profe == trainer and horarioClase == horarioArea:
                disponible = False
                print("El trainer se encuentra ocupado en este horario")
                break
        if disponible:
            listaAreas[opcion-1]['ruta'] = listaRutas[opcion2-1]['nombre']
            listaAreas[opcion-1]['trainer'] = listaTrainers[opcion3-1]['nombre']
            listaAreas[opcion-1]['fechaInicio']=fechaInicio
            listaAreas[opcion-1]['fechaSalida']=fechaFinalizacion
            jsonCRUD.guardarDatos(listaAreas,"areaEntrenamiento.json")
    else:
        print("No hay trainers inscritos")

asignarRuta()
