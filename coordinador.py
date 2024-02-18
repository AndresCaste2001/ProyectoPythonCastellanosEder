import jsonCRUD

def registrarNota():
    listaCamper = jsonCRUD.cargarDatos("campers.json")
    print("---- LISTA DE ESTUDIANTES ----\n\n")
    for index, camper in enumerate(listaCamper):
        nombre = camper.get('nombre','No hay nombre')
        apellido = camper.get('apellido','No hay apellido')
        if camper['estado']=="En proceso de ingreso":
            print(f"{index+1} - {nombre} {apellido}")
            
    numEstudiante = int(input("Digita el numero del camper que deseas registrarle nota: "))
    nota1 = int(input("Ingresa el valor de la primera nota: "))
    nota2 = int(input("Ingresa el valor de la segunda nota: "))
    promedio = (nota1+nota2)/2
    if(promedio>=60 and promedio<=100):
        listaCamper[numEstudiante-1]['estado']="aprobado"
    elif (promedio<60 and promedio>=0):
        listaCamper[numEstudiante-1]['estado']="inscrito"
    else:
        print("notas invalidas, debe estar en el rango de 0-100")
    jsonCRUD.guardarDatos(listaCamper,"campers.json")
        
def asignarArea():
    listaArea = jsonCRUD.cargarDatos("areaEntrenamiento.json")
    listaCampers = jsonCRUD.cargarDatos("campers.json")
    print("Los siguientes campers estan aprobados: ")
    for index,camper in enumerate(listaCampers):
        nombre  = camper.get('nombre', 'sin nombre')
        apellido = camper.get('apellido','sin apellido')
        if camper['estado']=="aprobado":
            print(f"{index+1}- {nombre} {apellido} ")
    opcion = int(input("ingresa el indice del camper: "))
    if listaCampers[opcion-1]['estado']=="aprobado":
        print("Las siguientes areas estan libres: ")
        for index2,area in enumerate(listaArea):
            if area['cuposClases']<=33:
                opcArea = area.get('nombre','no tiene nombre')
                opcCupo = area.get('cuposClases','cupo no disponible')
                opcRuta = area.get('ruta','sin ruta')
                print(f"{index2+1} nombre: {opcArea} - cupo: {opcCupo} - ruta: {opcRuta}")
        opcion2 = int(input("Ingresa el indice del salon que quieres registrar el camper: "))

        contador = listaArea[opcion2-1]['cuposClases']
        contador += 1
        listaArea[opcion2-1]['cuposClases'] = contador
        listaCampers[opcion-1]['salon'] = listaArea[opcion2-1]['nombre']
        listaCampers[opcion-1]['estado'] = "Cursando"

        jsonCRUD.guardarDatos(listaCampers,"campers.json")
        jsonCRUD.guardarDatos(listaArea,"areaEntrenamiento.json")
    else:
        print("El estudiante ingresado, no se encuentra en estado 'aprobado'")

def crearTrainer():
    listaTrainer = jsonCRUD.cargarDatos("trainer.json")
    nombre = input("Ingresa el nombre del trainer: ")
    trainer = {'nombre':nombre}
    listaTrainer.append(trainer)
    jsonCRUD.guardarDatos(listaTrainer,"trainer.json")

crearTrainer()