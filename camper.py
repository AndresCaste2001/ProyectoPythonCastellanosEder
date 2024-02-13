import json

def creacionCamper():
    lista = []
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
            break
        except ValueError:
            print("porfavor ingresa valores correctos")
    lista.append({'documento':documento,'nombre':nombre,'apellido':apellido,'direccion':direccion,'acudiente':acudiente,'telefono':telefono,'celular':celular,'estado':estado,'riesgo':riesgo})
    try:
        with open('campers.json', 'r') as campers:
            jsonCampers = json.load(campers)
    except(FileNotFoundError, json.decoder.JSONDecodeError):
        jsonCampers = []
    jsonCampers.extend(lista)
    with open('campers.json','w') as camp:
        json.dump(jsonCampers,camp,indent=4)
        print("agregado con exito al archivo json")
    

creacionCamper()

