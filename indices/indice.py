import requests 
from bs4 import BeautifulSoup 
from tabulate import tabulate



class Indices_economicos:

    def __init__(self) -> None:
        self.cronista = 'https://www.cronista.com/'
        self.puente = "https://www.puentenet.com/cotizaciones/riesgo-pais"
        self.portafolio = "https://www.portfoliopersonal.com/Cotizaciones/Bonos"


    def soup_validator(self, url, timeout=5, headers=None):
        """Retorna el HTML parseado o None en caso de error."""
        default_headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko)'
        }
        if headers:
            default_headers.update(headers)
        
        try:
            response = requests.get(url, headers=default_headers, timeout=timeout)
            response.raise_for_status()
    
        except (requests.exceptions.HTTPError, requests.exceptions.Timeout, requests.exceptions.ConnectionError) as error:
            return None
            
        try:
            soup = BeautifulSoup(response.content, "html.parser")
        except:
            return None
            
        return soup

    def dolares(self):
        monedas = ["Dolar Blue", "Dolar BNA", "Dolar CCL", "Dolar Tarjeta"]
        count = 0

        soup = self.soup_validator(self.cronista)
        value = soup.find_all('span', attrs={'class':'value'})

        for i in value:
            if count <= 3:
                print(f"{monedas[count]} {i.text}")
                count += 1

    def riesgo_pais(self):
        soup = self.soup_validator(self.puente)
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
        soup = self.soup_validator(self.portafolio)
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



    






