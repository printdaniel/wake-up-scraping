from indices.indice import Indices_economicos


app = Indices_economicos()

di = {
        "dolares": app.dolares,
        "bonos": app.bonos,
        "riesgo": app.riesgo_pais
        }

opciones = ["dolares", "bonos", "riesgo"]


def main():
    while True:

        entrada = input("Elige una opción: ")
        
        if entrada in opciones:
            di[entrada]()



if __name__ == '__main__':
    main()
