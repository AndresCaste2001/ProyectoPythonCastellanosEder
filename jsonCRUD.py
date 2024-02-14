import json

def cargarDatos(archivo):
    try:
        with open(archivo, "r") as file:
            jsonCampers = json.load(file)
            return jsonCampers
    except(FileNotFoundError, json.decoder.JSONDecodeError):
        jsonCampers = []
        return jsonCampers
    
def guardarDatos(datos, archivo):
    with open(archivo, "w") as file:
        escritura = json.dumps(datos, indent=4)
        file.write(escritura)
        print("agregado con exito al archivo json")