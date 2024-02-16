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
    if(promedio>=60):
        listaCamper[numEstudiante-1]['estado']="aprobado"
    jsonCRUD.guardarDatos(listaCamper,"campers.json")
        
registrarNota()