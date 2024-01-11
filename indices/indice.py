import requests 
from bs4 import BeautifulSoup 
from tabulate import tabulate


class Indices_economicos:
    def __init__(self) -> None:
        self.cronista = 'https://www.cronista.com/'
        self.puente = "https://www.puentenet.com/cotizaciones/riesgo-pais"
        self.portafolio = "https://www.portfoliopersonal.com/Cotizaciones/Bonos"

    def _soup_validator(self, url, timeout=5, headers=None):
        """Retorna el HTML parseado o None en caso de error."""
        default_headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko)'
        }
        if headers:
            default_headers.update(headers)

        try:
            response = requests.get(url, headers=default_headers, timeout=timeout)
            response.raise_for_status()
            soup = BeautifulSoup(response.content, "html.parser")
            return soup

        except requests.exceptions.RequestException as e:
            print(f"Error al hacer la solicitud: {e}")
            return None

        except Exception as e:
            print(f"Error inesperado: {e}")
            return None

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



    






