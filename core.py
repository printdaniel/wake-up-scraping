from diccionario import opciones
from indices.indice import Indices_economicos
from colorama import init, Fore

app = Indices_economicos()
init()

def opciones_menu():
    print(Fore.RED + "Indices Económicos: Dolares, Bonos, Riesgo")
    print(Fore.BLUE + "Cine: Populares,")


def ejecutar_menu():
    opciones_menu()

    while True:

        entrada = input(Fore.YELLOW + "Elige una opción: ").lower()
        
        if entrada in list(opciones.keys()):
            opciones[entrada]()
        elif entrada == "opciones":
            opciones_menu()
        elif entrada == "exit":
            print(Fore.BLUE + "Bye")
            break
        else:
            print(Fore.RED + "Opción no válida")
