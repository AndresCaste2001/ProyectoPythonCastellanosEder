import jsonCRUD
def creacionRuta():
    listaRutas = jsonCRUD.cargarDatos("rutas.json")
    while True:
        print("*********************************************")
        print("Bienvenido a la seccion de creacion de rutas")
        print("*********************************************\n\n")
        fundamentos = []
        programacionWeb = []
        progFormal = []
        basesDatos = []
        backend = []
        try:
            nombre = input("Ingrese el nombre de la ruta: ")
            print("Ingrese tecnologias a usar en fundamentos de programacion \nIngresa 0 para finalizar..")
            while True:
                tecnologia = input()
                if tecnologia == "0":
                    break
                else:
                    fundamentos.append(tecnologia)
            print("Ingrese tecnologias a usar en programacion web: \nIngresa 0 para finalizar..")
            while True:
                tecnologia = input()
                if tecnologia == "0":
                    break
                else:
                    programacionWeb.append(tecnologia)
            print("Ingrese tecnologias a usar en programacion formal: \nIngresa 0 para finalizar..")
            while True:
                tecnologia = input()
                if tecnologia == "0":
                    break
                else:
                    progFormal.append(tecnologia)
            print("Ingrese tecnologias a usar en Bases de datos: \nIngresa 0 para finalizar..")
            while True:
                tecnologia = input()
                if tecnologia == "0":
                    break
                else:
                    basesDatos.append(tecnologia)
            print("Ingrese tecnologias a usar en backend: \nIngresa 0 para finalizar..")
            while True:
                tecnologia = input()
                if tecnologia == "0":
                    break
                else:
                    backend.append(tecnologia)
            break
        except ValueError:
            print("\nERROR: Por favor ingrese un valor valido.")
            
    listaRutas.append({'nombre':nombre,'fundamentos':fundamentos, 'programacionWeb':programacionWeb, 'progFormal':progFormal, 'basesDatos':basesDatos,'backend':backend})
    jsonCRUD.guardarDatos(listaRutas,"rutas.json")
    print(listaRutas)
creacionRuta()