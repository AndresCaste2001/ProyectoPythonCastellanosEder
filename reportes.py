import jsonCRUD

def CampersInscritos():
    listaCampers = jsonCRUD.cargarDatos("campers.json")
    camperInscrito = any("Inscrito" in campers['estado'] for campers in listaCampers)
    if camperInscrito:
        print("--- Lista Inscritos ---")
        for camper in listaCampers:
            estado = camper.get('estado','sin estado')
            nombre = camper.get('nombre','sin nombre')
            apellido = camper.get('apellido','sin apellido')
            if estado == "Inscrito":
                print(f"{nombre} {apellido}")
    else:
        print("No se encuentran Campers Inscritos")

def CampersAprobados():
    listaCampers = jsonCRUD.cargarDatos("campers.json")
    camperAprobado = any("Aprobado" in camper['estado'] for camper in listaCampers)
    if camperAprobado:
        print("--- Lista Aprobados ---")
        for camper in listaCampers:
            nombre  = camper.get('nombre', 'sin nombre')
            apellido = camper.get('apellido','sin apellido')
            if camper['estado']=="Aprobado":
                print(f"{nombre} {apellido}")
    else:
        print("No se encuentran Campers Aprobados")

def mostrarTrainers():
    listaTrainers = jsonCRUD.cargarDatos("trainer.json")
    if listaTrainers:
        for trainer in listaTrainers:
            nombre = trainer.get('nombre','no hay nombre')
            apellido = trainer.get('apellido','no hay apellido')
            documento = trainer.get('documento','no hay documento')
            print(f"nommbre:  {nombre} - apellido:{apellido} - documento: {documento}")

def CampersBajoRendimiento():
    listaCampers = jsonCRUD.cargarDatos("campers.json")
    camperRiesgo = any("Alto" in campers['riesgo'] for campers in listaCampers)
    if camperRiesgo:
        print("--- Lista Bajo Rendimiento ---")
        for camper in listaCampers:
            riesgo = camper.get('riesgo','sin estado')
            nombre = camper.get('nombre','sin nombre')
            apellido = camper.get('apellido','sin apellido')
            if riesgo == "Alto":
                print(f"{nombre} {apellido}")
    else:
        print("No se encuentran Campers con bajo rendimiento")

def mostrarCamperTrainerRuta():
    listaRutas = jsonCRUD.cargarDatos("rutas.json")
    listaCampers = jsonCRUD.cargarDatos("campers.json")
    listaArea = jsonCRUD.cargarDatos("areaEntrenamiento.json")

    print("--- Rutas Existentes ---")
    for index,ruta in enumerate(listaRutas):
        nombre = ruta.get('nombre','no hay nombre')
        print(f"{index+1} - {nombre}")
    opcion = int(input("Ingrese la ruta que desea analizar: "))   
    nombreRuta = listaRutas[opcion-1]['nombre']

    for area in listaArea:
        rutaAsignada = area.get('ruta','no hay ruta')
        trainer = area.get('trainer','no existe trainer')
        nombre = area.get('nombre','no hay salon')
        if rutaAsignada == nombreRuta:
            print(f"--- {nombre} ---")
            print(f"para la ruta {nombreRuta} el trainer es {trainer}")
            print("--- lista estudiantes asociados ---")
            for camper in listaCampers:
                nombre = camper.get('nombre','no existe nombre')
                apellido = camper.get('apellido','no existe apellido')
                salon = camper.get('salon','no hay salon')
                if salon == rutaAsignada:
                    print(f"{nombre} {apellido}")

def mostrarModulosPerdidos():
    listaCampers = jsonCRUD.cargarDatos("campers.json")
    listaArea = jsonCRUD.cargarDatos("areaEntrenamiento.json")
    listaRutas = jsonCRUD.cargarDatos("rutas.json")
    listaCampersAprobado = {'primerModulo':[],'segundoModulo':[],'tercerModulo':[],'cuartoModulo':[],'quintoModulo':[]}
    listaCampersReprobado = {'primerModulo':[],'segundoModulo':[],'tercerModulo':[],'cuartoModulo':[],'quintoModulo':[]}

    for ruta in (listaRutas):
        nombreR = ruta.get('nombre','no hay nombre')
        print(f"************** {nombreR} **************")
        for  area in listaArea:
            rutaA = area.get('ruta','no existe ruta')
            nombreA = area.get('nombre','nombre no existe')
            trainerA = area.get('trainer','no existe trainer')
            if rutaA == nombreR:
                print(f"trainer:  {trainerA}")
                for camper in listaCampers:
                    nombreC = camper.get('nombre','no existe nombre')
                    apellidoC = camper.get('apellido','no existe apellido')
                    salonC = camper.get('salon','no existe salon')
                    notas = camper.get('nota','nota no encontrada')
                    if salonC == nombreA:
                            
                            if (notas[0])>=60:
                                listaCampersAprobado['primerModulo'].append({'nombre':nombreC,'apellido':apellidoC,'nota':notas[0]})
                            else:
                                listaCampersReprobado['primerModulo'].append({'nombre':nombreC,'apellido':apellidoC,'nota':notas[0]})
                            if notas[1]>=60:
                                listaCampersAprobado['segundoModulo'].append({'nombre':nombreC,'apellido':apellidoC,'nota':notas[1]})
                            else:
                                listaCampersReprobado['segundoModulo'].append({'nombre':nombreC,'apellido':apellidoC,'nota':notas[1]})
                            if notas[2] >= 60:
                                listaCampersAprobado['tercerModulo'].append({'nombre': nombreC, 'apellido': apellidoC,'nota':notas[2]})
                            else:
                                listaCampersReprobado['tercerModulo'].append({'nombre': nombreC, 'apellido': apellidoC,'nota':notas[2]})
                            if notas[3] >= 60:
                                listaCampersAprobado['cuartoModulo'].append({'nombre': nombreC, 'apellido': apellidoC,'nota':notas[3]})
                            else:
                                listaCampersReprobado['cuartoModulo'].append({'nombre': nombreC, 'apellido': apellidoC,'nota':notas[3]})
                            if notas[4] >= 60:
                                listaCampersAprobado['quintoModulo'].append({'nombre': nombreC, 'apellido': apellidoC,'nota':notas[4]})
                            else:
                                listaCampersReprobado['quintoModulo'].append({'nombre': nombreC, 'apellido': apellidoC,'nota':notas[4]})                            
                            print("\t\t\t--- Primer Modulo ---")
                            print("aprobados:")
                            for x in listaCampersAprobado['primerModulo']:
                                nombre = x.get('nombre')
                                apellido = x.get('apellido')
                                nota = x.get('nota')            
                                print(f"{nombre} {apellido} - {nota}")
                            print("reprobados:")
                            for x in listaCampersReprobado['primerModulo']:            
                                nombre = x.get('nombre')
                                apellido = x.get('apellido')
                                nota = x.get('nota')            
                                print(f"{nombre} {apellido} - {nota}")

                            print("\t\t\t--- segundo modulo ---")
                            print("aprobados:")
                            for x in listaCampersAprobado['segundoModulo']:            
                                nombre = x.get('nombre')
                                apellido = x.get('apellido')
                                nota = x.get('nota')            
                                print(f"{nombre} {apellido} - {nota}")
                            print("reprobados:")
                            for x in listaCampersReprobado['segundoModulo']:            
                                nombre = x.get('nombre')
                                apellido = x.get('apellido')
                                nota = x.get('nota')            
                                print(f"{nombre} {apellido} - {nota}") 

                            print("\t\t\t--- tercer modulo ---")
                            print("aprobados:")
                            for x in listaCampersAprobado['tercerModulo']:            
                                nombre = x.get('nombre')
                                apellido = x.get('apellido')
                                nota = x.get('nota')            
                                print(f"{nombre} {apellido} - {nota}")
                            print("reprobados:")
                            for x in listaCampersReprobado['tercerModulo']:            
                                nombre = x.get('nombre')
                                apellido = x.get('apellido')
                                nota = x.get('nota')            
                                print(f"{nombre} {apellido} - {nota}")

                            print("\t\t\t--- cuarto modulo ---")
                            print("aprobados:")
                            for x in listaCampersAprobado['cuartoModulo']:            
                                nombre = x.get('nombre')
                                apellido = x.get('apellido')
                                nota = x.get('nota')            
                                print(f"{nombre} {apellido} - {nota}")
                            print("reprobados:")
                            for x in listaCampersReprobado['cuartoModulo']:            
                                nombre = x.get('nombre')
                                apellido = x.get('apellido')
                                nota = x.get('nota')            
                                print(f"{nombre} {apellido} - {nota}")

                            print("\t\t\t--- quinto modulo ---")
                            print("aprobados:")
                            for x in listaCampersAprobado['quintoModulo']:            
                                nombre = x.get('nombre')
                                apellido = x.get('apellido')
                                nota = x.get('nota')            
                                print(f"{nombre} {apellido} - {nota}")
                            print("reprobados:")
                            for x in listaCampersReprobado['quintoModulo']:            
                                nombre = x.get('nombre')
                                apellido = x.get('apellido')
                                nota = x.get('nota')            
                                print(f"{nombre} {apellido} - {nota}")
                            listaCampersAprobado = {'primerModulo':[],'segundoModulo':[],'tercerModulo':[],'cuartoModulo':[],'quintoModulo':[]}
                            listaCampersReprobado = {'primerModulo':[],'segundoModulo':[],'tercerModulo':[],'cuartoModulo':[],'quintoModulo':[]}