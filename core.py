from diccionario import opciones
from indices.indice import Indices_economicos



app = Indices_economicos()


def ejecutar_menu():
    while True:

        entrada = input("Elige una opción: ").lower()
        
        if entrada in list(opciones.keys()):
            opciones[entrada]()
        else:
            print("Opción no válida")
