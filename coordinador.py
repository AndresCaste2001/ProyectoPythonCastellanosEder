import jsonCRUD
import time

def registrarNota():
    while True:
        listaCamper = jsonCRUD.cargarDatos("campers.json")
        campersIngreso = any("En proceso de ingreso" in campers['estado'] for campers in listaCamper)
        if campersIngreso:
            print("---- LISTA DE ESTUDIANTES ----\n\n")
            for index, camper in enumerate(listaCamper):
                nombre = camper.get('nombre','No hay nombre')
                apellido = camper.get('apellido','No hay apellido')
                if camper['estado']=="En proceso de ingreso":
                    print(f"{index+1} - {nombre} {apellido}")
            try:
                numEstudiante = int(input("Digita el indice del camper que deseas registrarle nota: "))
            except ValueError:
                print("\n***ingresa una opcion correcta***")
                time.sleep(2)
                continue
            if listaCamper[numEstudiante-1]['estado']=="En proceso de ingreso":
                try:
                    nota1 = int(input("Ingresa la nota teorica: "))
                    nota2 = int(input("Ingresa la nota practica: "))
                except ValueError:
                    print("\n***ingresa una opcion correcta***")
                    time.sleep(2)
                    continue
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
        break
        
def asignarArea():
    while True:
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
            try:
                opcion = int(input("ingresa el indice del camper: "))
            except ValueError:
                print("\n***ingresa una opcion correcta***")
                time.sleep(2)
                continue
            if listaCampers[opcion-1]['estado']=="Aprobado":

                print("Las siguientes areas estan libres: ")
                for index2,area in enumerate(listaArea):
                    if area['cuposClases']<33:
                        opcArea = area.get('nombre','no tiene nombre')
                        opcCupo = area.get('cuposClases','cupo no disponible')
                        opcRuta = area.get('ruta','sin ruta')
                        print(f"{index2+1} nombre: {opcArea} - cupo: {33-opcCupo} - ruta: {opcRuta}")
                try:
                    opcion2 = int(input("Ingresa el indice del salon que quieres registrar el camper: "))
                except ValueError:
                    print("\n***ingresa una opcion correcta***")
                    time.sleep(2)
                    continue
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
        break

def crearTrainer():
    while True:
        try:
            listaTrainer = jsonCRUD.cargarDatos("trainer.json")
            nombre = input("Ingresa el nombre del trainer: ")
            apellido = input("Ingresa el apellido del trainer: ")
            documento = int(input("Ingresa el numero de documento: "))
        except ValueError:
                print("\n***ingresa una opcion correcta***")
                time.sleep(2)
                continue
        trainer = {'nombre':nombre,'apellido':apellido,'documento':documento}
        listaTrainer.append(trainer)
        jsonCRUD.guardarDatos(listaTrainer,"trainer.json")
        break

