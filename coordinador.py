import jsonCRUD

def registrarNota():
    listaCamper = jsonCRUD.cargarDatos("campers.json")
    campersIngreso = any("En proceso de ingreso" in campers['estado'] for campers in listaCamper)
    if campersIngreso:
        print("---- LISTA DE ESTUDIANTES ----\n\n")
        for index, camper in enumerate(listaCamper):
            nombre = camper.get('nombre','No hay nombre')
            apellido = camper.get('apellido','No hay apellido')
            if camper['estado']=="En proceso de ingreso":
                print(f"{index+1} - {nombre} {apellido}")
                
        numEstudiante = int(input("Digita el indice del camper que deseas registrarle nota: "))
        if listaCamper[numEstudiante-1]['estado']=="En proceso de ingreso":
            nota1 = int(input("Ingresa el valor de la primera nota: "))
            nota2 = int(input("Ingresa el valor de la segunda nota: "))
            promedio = (nota1+nota2)/2
            if(promedio>=60 and promedio<=100):
                listaCamper[numEstudiante-1]['estado']="Aprobado"
            elif (promedio<60 and promedio>=0):
                listaCamper[numEstudiante-1]['estado']="Inscrito"
            else:
                print("notas invalidas, debe estar en el rango de 0-100")
            jsonCRUD.guardarDatos(listaCamper,"campers.json")
            print(f"su promedio fue {promedio}")
        else:
            "Ingrese un indice en la lista"
    else:
        print("No hay campers en proceso de Ingreso")
        
def asignarArea():
    listaArea = jsonCRUD.cargarDatos("areaEntrenamiento.json")
    listaCampers = jsonCRUD.cargarDatos("campers.json")
    camperAprobado = any("Aprobado" in camper['estado'] for camper in listaCampers)

    if camperAprobado:

        print("Los siguientes campers estan aprobados: ")
        for index,camper in enumerate(listaCampers):
            nombre  = camper.get('nombre', 'sin nombre')
            apellido = camper.get('apellido','sin apellido')
            if camper['estado']=="Aprobado":
                print(f"{index+1}- {nombre} {apellido} ")
        opcion = int(input("ingresa el indice del camper: "))

        if listaCampers[opcion-1]['estado']=="Aprobado":

            print("Las siguientes areas estan libres: ")
            for index2,area in enumerate(listaArea):
                if area['cuposClases']<33:
                    opcArea = area.get('nombre','no tiene nombre')
                    opcCupo = area.get('cuposClases','cupo no disponible')
                    opcRuta = area.get('ruta','sin ruta')
                    print(f"{index2+1} nombre: {opcArea} - cupo: {33-opcCupo} - ruta: {opcRuta}")
            opcion2 = int(input("Ingresa el indice del salon que quieres registrar el camper: "))

            if listaArea[opcion2-1]['cuposClases']<33:

                contador = listaArea[opcion2-1]['cuposClases']
                contador += 1
                listaArea[opcion2-1]['cuposClases'] = contador
                listaCampers[opcion-1]['salon'] = listaArea[opcion2-1]['nombre']
                listaCampers[opcion-1]['estado'] = "Cursando"

                jsonCRUD.guardarDatos(listaCampers,"campers.json")
                jsonCRUD.guardarDatos(listaArea,"areaEntrenamiento.json")
            else:
                print("Clase llena!")
        else:
            print("Ingrese un indice dentro de la lista")
    else:
        print("No hay campers aprobados")

def crearTrainer():
    listaTrainer = jsonCRUD.cargarDatos("trainer.json")
    nombre = input("Ingresa el nombre del trainer: ")
    apellido = input("Ingresa el apellido del trainer: ")
    documento = int(input("Ingresa el numero de documento: "))
    trainer = {'nombre':nombre,'apellido':apellido,'documento':documento}
    listaTrainer.append(trainer)
    jsonCRUD.guardarDatos(listaTrainer,"trainer.json")

asignarArea()