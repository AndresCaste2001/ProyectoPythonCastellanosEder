import json
def cargarDatos():
    try:
        with open("campers.json", "r") as file:
            jsonCampers = json.load(file)
            return jsonCampers
    except(FileNotFoundError, json.decoder.JSONDecodeError):
        jsonCampers = []
        return jsonCampers
    
def guardarDatos(datos):
    with open("campers.json", "w") as file:
        escritura = json.dumps(datos, indent=4)
        file.write(escritura)
        print("agregado con exito al archivo json")