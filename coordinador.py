import jsonCRUD

def registrarNota():
    listaCamper = jsonCRUD("campers.json")
    print("---- LISTA DE ESTUDIANTES ----\n\n")
    for index, camper in enumerate(listaCamper):
        nombre = camper.get('nombre','No hay nombre')
        apellido = camper.get('apellido','No hay apellido')
        print(f"{index+1} - {nombre} {apellido}")
    