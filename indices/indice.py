import requests 
from bs4 import BeautifulSoup 
from tabulate import tabulate
from base_parser import BaseParser

class Indices_economicos(BaseParser):
    def __init__(self) -> None:
        self.cronista = 'https://www.cronista.com/'
        self.puente = "https://www.puentenet.com/cotizaciones/riesgo-pais"
        self.portafolio = "https://www.portfoliopersonal.com/Cotizaciones/Bonos"
        self.datos_macro_ipc ="https://datosmacro.expansion.com/ipc-paises/argentina"

    def dolares(self):
        """
        Método que extrae y muestra información sobre distintas cotizaciones de dólares.

        El método utiliza la biblioteca BeautifulSoup para realizar scraping en un sitio web
        y encuentra los elementos HTML que contienen la información de las cotizaciones.

        Las cotizaciones se imprimen en la consola junto con el nombre de la moneda correspondiente.

        Este método asume que la estructura del sitio web y las clases HTML utilizadas no cambian
        de manera significativa.

        :return: No devuelve ningún valor, imprime las cotizaciones en la consola.
        """
        # Nombre de las distintas monedas o valores del dólar
        monedas = ["Dolar Blue", "Dolar BNA", "Dolar CCL", "Dolar Tarjeta"]
        count = 0

        # Obtener el contenido HTML y validar con BeautifulSoup
        soup = self._soup_validator(self.cronista)
        value = soup.find_all('span', attrs={'class':'value'})

        # Iterar todos los elementos encontrados
        for i in value:
            if count <= 3:
                print(f"{monedas[count]} {i.text}")
                count += 1


    def riesgo_pais(self):
        soup = self._soup_validator(self.puente)
        table = soup.find('table')

        # Lista para almacenar las filas de la tabla
        filas = []

        for fila in table.find_all('tr'):
            # Lista para almacenar las celdas de cada fila
            celdas = []

            for celda in fila.find_all('td'):
                # Extraer el contenido de la celda y eliminar espacios en blanco
                contenido_celda = celda.text.strip()
                # Agregar el contenido de la celda a la lista de celdas
                celdas.append(contenido_celda)

            # Agregar la lista de celdas a la lista de filas
            filas.append(celdas)

        # Imprimir la tabla formateada
        print(tabulate(filas, headers='firstrow', tablefmt='grid'))


    def bonos(self):
        soup = self._soup_validator(self.portafolio)
        table = soup.find('table')

        # Lista para almacenar las filas de la tabla
        filas = []

        for fila in table.find_all('tr'):
            # Lista para almacenar las celdas de cada fila
            celdas = []

            for celda in fila.find_all('td'):
                # Extraer el contenido de la celda y eliminar espacios en blanco
                contenido_celda = celda.text.strip()
                # Agregar el contenido de la celda a la lista de celdas
                celdas.append(contenido_celda)

            # Agregar la lista de celdas a la lista de filas
            filas.append(celdas)

        # Imprimir la tabla formateada
        print(tabulate(filas, headers='firstrow', tablefmt='grid'))

    
