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
            break
        except ValueError:
            print("porfavor ingresa valores correctos")
    listaCampers.append({'documento':documento,'nombre':nombre,'apellido':apellido,'direccion':direccion,'acudiente':acudiente,'telefono':telefono,'celular':celular,'estado':estado,'riesgo':riesgo,'ruta':ruta})
    jsonCRUD.guardarDatos(listaCampers,"campers.json")
    
creacionCamper()


