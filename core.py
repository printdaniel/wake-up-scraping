from diccionario import opciones
from indices.indice import Indices_economicos
from colorama import init, Fore



app = Indices_economicos()
init()

def opciones_menu():
    print(Fore.RED + "Indices Económicos: Dolares, Bonos, Riesgo")


def ejecutar_menu():
    opciones_menu()
    while True:

        entrada = input(Fore.YELLOW + "Elige una opción: ").lower()
        
        if entrada in list(opciones.keys()):
            opciones[entrada]()
        elif entrada == "exit":
            break
        else:
            print("Opción no válida")
