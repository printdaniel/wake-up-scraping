from diccionario import opciones_dict
from colorama import init, Fore

init()

def opciones_menu():
    print(Fore.RED + "Indices Económicos: Dolares, Bonos, Riesgo")
    print(Fore.BLUE + "Cine: Populares, Lanzamientos")
    print(Fore.GREEN + "Para salir: exit")


def ejecutar_menu():
    opciones_menu()

    while True:

        entrada = input(Fore.YELLOW + "Elige una opción: ").lower()
        
        try:
            if entrada in list(opciones_dict.keys()):
                opciones_dict[entrada]()
            elif entrada == "opciones":
                opciones_menu()
            elif entrada == "exit":
                print(Fore.BLUE + "Bye")
                break
            else:
                print(Fore.RED + "Opción no válida")
        except Exception as e:
            print(Fore.RED + f"Error inesperado: {e}")
