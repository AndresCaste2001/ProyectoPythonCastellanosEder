import jsonCRUD

def notaModulo():
    notaTeorica = 0
    notaPractica = 0
    notaTrainer = 0
    listaCampers = jsonCRUD.cargarDatos("campers.json")
    camperCursando = any("Cursando" in camper['estado'] for camper in listaCampers)
    if camperCursando:
        print("--- Asignar Nota Modulos ---")
        contadorModulo = 0
        print("puedes asignar notas a los siguientes campers: ")
        for index,camper in enumerate(listaCampers):
            nombre  = camper.get('nombre', 'sin nombre')
            apellido = camper.get('apellido','sin apellido')
            if camper['estado']=="Cursando":
                print(f"{index+1}- {nombre} {apellido} ")
        opcion = int(input("ingresa el indice del camper: "))

        if listaCampers[opcion-1]['estado']=="Cursando":

            for nota in listaCampers[opcion-1]['nota']:
                if nota == 0:
                    print(f"Asignando nota Modulo {contadorModulo+1}")
                    notaTeorica = int(input("Ingrese la nota teorica: "))
                    notaPractica = int(input("Ingrese la nota practica: "))
                    notaTrainer = int(input("Ingrese la nota del trainer: "))
                    break
                else:
                        contadorModulo += 1
                print (contadorModulo)

            if contadorModulo == 4 and listaCampers[opcion-1]['riesgo']== "Bajo":
                    listaCampers[opcion-1]['estado'] = "Graduado"

            if all(var >= 0 and var<=100 for var in (notaTeorica, notaPractica, notaTrainer)):
                notaModulo = ((notaTeorica*0.3)+(notaPractica*0.6)+(notaTrainer*0.1))
                if notaModulo<60:
                    listaCampers[opcion-1]['riesgo'] = "Alto"
                listaCampers[opcion-1]['nota'][contadorModulo]=notaModulo
                print(f"La nota final del modulo es: {notaModulo}")
                jsonCRUD.guardarDatos(listaCampers,"campers.json")        
            else:
                print("Notas no validas")
        else:
            print("Ingresa un indice que este dentro de la lista")
    else:
        print("No hay campers cursando!")
notaModulo()
