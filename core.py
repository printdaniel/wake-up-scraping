from diccionario import opciones_dict
from colorama import init, Fore
from tabulate import tabulate

init()

def opciones_menu():
    menu_options = [
        [Fore.RED + "Indices Económicos", "Dolares, Bonos, Riesgo"],
        [Fore.BLUE + "Cine", "Populares, Lanzamientos, Taquilleras"],
        [Fore.YELLOW + "Noticias", "Pagina, Infobae, Tiempo"],
        [Fore.GREEN + "Para salir", "exit"]
    ]
    table = tabulate(menu_options, headers=["Categoría", "Opciones"], tablefmt="fancy_grid")
    print(table)
   
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
