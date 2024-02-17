import json
import jsonCRUD


def creacionCamper():
    listaCampers = []
    listaCampers = jsonCRUD.cargarDatos("campers.json")
    
    while True:
        try:
            documento = int(input("digita el numero de identificacion: \n"))
            nombre = input("Ingresa el nombre: \n")
            apellido = input("Ingresa el apellido: \n")
            direccion = input("Ingresa la direccion: \n")
            acudiente = input("Ingrese el nombre de su acudiente: \n")
            telefono = int(input("Ingrese un telefono  fijo: \n"))
            celular = int(input("Ingrese un telefono movil: \n"))
            estado = "En proceso de ingreso"
            riesgo = ""
            ruta = ""
            notas = [0,0,0,0,0]
            break
        except ValueError:
            print("porfavor ingresa valores correctos")
    listaCampers.append({'documento':documento,'nombre':nombre,'apellido':apellido,'direccion':direccion,'acudiente':acudiente,'telefono':telefono,'celular':celular,'estado':estado,'riesgo':riesgo,'ruta':ruta})
    jsonCRUD.guardarDatos(listaCampers,"campers.json")
 
def asignarArea():
    listaArea = jsonCRUD.cargarDatos("areaEntrenamiento.json")
    listaCampers = jsonCRUD.cargarDatos("campers.json")
    for index,camper in enumerate(listaCampers):
        nombre  = camper.get('nombre', 'sin nombre')
        apellido = camper.get('apellido','sin apellido')
        if camper['estado']=="aprobado":
            print("Los siguientes campers estan aprobados: ")
            print(f"{index+1}- {nombre} {apellido} ")
    opcion = int(input("ingresa el indice del camper: "))
    print("Las siguientes areas estan libres: ")
    for index2,area in enumerate(listaArea):
        if area['cuposClases']<=33:
            opcArea = area['nombre']
            opcCupo = area['cuposClases']
            print(f"{index2} nombre : {opcArea} --- cupo: {opcCupo}")
    opcion = int(input("Ingresa el indice del salon que quieres registrar el camper: "))

creacionCamper()