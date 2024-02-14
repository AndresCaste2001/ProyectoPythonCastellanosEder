import jsonCRUD
def creacionRuta():
    listaRutas = jsonCRUD.cargarDatos("rutas.py")
    while True:
        print("*********************************************")
        print("Bienvenido a la seccion de creacion de rutas")
        print("*********************************************\n\n")
        fundamentos = []
        programacionWeb = []
        programacionFormal = []
        basesDatos = []
        backEnd = []
        try:
            nombre = input("Ingrese el nombre de la ruta: ")
            programacionWeb.extend(input("Ingrese las tecnologias a usar en programacion web: "))
            
        except ValueError:
            print("\nERROR: Por favor ingrese un valor valido.")
            continue
    listaRutas.append({'nombre':nombre,'fundamentos':fundamentos})
creacionRuta()