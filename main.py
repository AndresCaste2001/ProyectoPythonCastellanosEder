import os
import camper
import time
import trainer
import coordinador
import rutas
import reportes
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

while True:
    clear()
    print("*****************************")
    print("  Bienvenidos al programa  ")
    print("*****************************")
    print("1.)Inscripcion Camper")
    print("2.)Seccion trainer")
    print("3.)Seccion Coordinacion")
    print("4.)Reportes")
    print("0.)Salir del programa")
    try:
        opc = int(input("\nIngresa una opcion: "))
    except ValueError:
        print("\n***ingresa una opcion correcta***")
        time.sleep(2)
        continue

    if opc == 1:
        clear()
        print("*****************************")
        print("--- Inscripciones Campers ---")
        print("*****************************")
        camper.creacionCamper()
    elif opc == 2:
        while True:
            clear()
            print("************************")
            print("--- Seccion trainer ---")
            print("************************")
            print("1.)Ingresar notas del modulo estudiantes")
            print("0.)Salir al menu principal")
            try:
                opc = int(input())
            except ValueError:
                print("\n***ingresa una opcion correcta***")
                time.sleep(2)
                continue
            if opc == 1:
                trainer.notaModulo()
            elif opc == 0:
                break
    elif opc == 3:
        while True:
            print("***************************")
            print("--- Seccion Coordinador ---")
            print("***************************")
            print("1.)Registrar notas de ingreso")
            print("2.)Asignar area a un camper")
            print("3.)Crear trainer")
            print("4.)Crear Ruta")
            print("5.)Asignar ruta a un area")
            print("0.)Salir al menu principal")
            try:
                opc = int(input())
            except ValueError:
                print("\n***ingresa una opcion correcta***")
                time.sleep(2)
                continue
            if opc == 1:
                coordinador.registrarNota()
            elif opc == 2:
                coordinador.asignarArea()
            elif opc == 3:
                coordinador.crearTrainer()
            elif opc == 4:
                rutas.creacionRuta()
            elif opc == 5:
                rutas.asignarRuta()
            elif opc == 0:
                break
    elif opc == 4:
        while True:
            print("*************************")
            print("--- Seccion Reportes ---")
            print("*************************")
            print("1.)Mostrar Campers Inscritos")
            print("2.)Mostrar Campers Aprobados")
            print("3.)Mostrar lista de Trainers")
            print("4.)Mostrar Campers con bajo rendimiento")
            print("5.)Mostrar Campers-Trainer de una ruta")
            print("6.)Mostrar aprobados y reprobados por ruta-modulo")
            print("0.)Salir")
            try:
                opc = int(input())
            except ValueError:
                print("\n***ingresa una opcion correcta***")
                time.sleep(2)
                continue
            if opc == 1:
                reportes.CampersInscritos()
            elif opc == 2:
                reportes.CampersAprobados()
            elif opc == 3:
                reportes.mostrarTrainers()
            elif opc == 4:
                reportes.CampersBajoRendimiento()
            elif opc == 5:
                reportes.mostrarCamperTrainerRuta()
            elif opc == 6:
                reportes.mostrarModulosPerdidos()
            elif opc == 0:
                break
    elif opc == 0:
        break
    


