from bs4 import BeautifulSoup 
from tabulate import tabulate
from base_parser import BaseParser


class Cine(BaseParser):

    def __init__(self) -> None:
        self.populares = "https://www.imdb.com/chart/moviemeter/?ref_=watch_tpks_chtmvm" 
        self.proximamente = "https://www.imdb.com/calendar/?ref_=rlm&region=AR&type=MOVIE"
        self.taquilleras_url = "https://www.imdb.com/chart/boxoffice/?ref_=nv_ch_cht"


    def peliculas_populares(self):
        soup = self._soup_validator(self.populares)

        # Encuentra el contenedor principal que rodea a los títulos de películas
        contenedor_peliculas = soup.find_all('h3', class_='ipc-title__text')
        count = 1

        if contenedor_peliculas:
            # Maneja posibles errores si no se encuentran títulos
            peliculas_p = [titulo.text for titulo in contenedor_peliculas]

            for title in peliculas_p[1:]:
                print(f" {count} {title}")
                count += 1
                if count == 21:
                    break
        else:
            print("No se encontraron títulos de películas.")


    def lanzamientos(self):
        """
        Muestra los títulos de lanzamientos próximos.

        Utiliza la información de la URL de próximos lanzamientos
        y muestra los títulos disponibles en la consola.

        Returns
        -------
        None
            No hay un valor de retorno específico.
        """
        soup = self._soup_validator(self.proximamente)
        elementos_a = soup.find_all('a', class_='ipc-metadata-list-summary-item__t')

        if elementos_a:
            next = [l.text for l in elementos_a]
            for title in next:
                print(f"{title}")
        else:
            print("No se encontrarios títulos")

    def taquilleras(self):
        """
        Muestra los títulos de películas taquilleras.

        Utiliza la información de la URL de películas taquilleras
        y muestra los títulos disponibles en la consola.

        Returns
        -------
        None
            No hay un valor de retorno específico.

        """
        soup = self._soup_validator(self.taquilleras_url)
        content = soup.find_all('h3', class_= 'ipc-title__text')

        count = 1
        if content:
            peliculas_t = [titulo.text for titulo in content]
            for title in peliculas_t:
                print(f"{title}")
                count += 1
                if count == 12:
                    break
        else:
            print("No se encontraron títulos de películas.")
