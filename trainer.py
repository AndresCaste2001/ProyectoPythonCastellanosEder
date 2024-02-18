import jsonCRUD

def notaModulo():
    listaCampers = jsonCRUD.cargarDatos("campers.json")
    print("--- Asignar Nota Modulos ---")
    contadorModulo = 0
    print("puedes asignar notas a los siguientes campers: ")
    for index,camper in enumerate(listaCampers):
        nombre  = camper.get('nombre', 'sin nombre')
        apellido = camper.get('apellido','sin apellido')
        if camper['estado']=="Cursando":
            print(f"{index+1}- {nombre} {apellido} ")
    opcion = int(input("ingresa el indice del camper: "))
                 
    for camper in listaCampers:
        nota = camper.get('notas')
        for x in nota:
            print(x)
