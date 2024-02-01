import requests 
from bs4 import BeautifulSoup 
from base_parser import BaseParser

class Clima(BaseParser):
    def __init__(self) -> None:
        self._meteored = 'https://www.meteored.com.ar/tiempo-en_Federal-America+Sur-Argentina-Entre+Rios--1-16689.html'
        self._acuweather = 'https://www.accuweather.com/es/ar/federal/9103/weather-forecast/9103'
        self._infoclima = 'https://infoclima.com/pronosticos/argentina/entre-rios/federal/' 


    def meteored(self):
        """ Retorna el estado y temperatura según el sitio meteored"""
        soup = self._soup_validator(self._meteored)
        temp_data = soup.find_all('span',attrs={'class':'dato-temperatura changeUnitT'})
        estado_data = soup.find_all('span',attrs={'descripcion'})
        
        for e in estado_data:
            self.meteored_e = e.text
        for i in temp_data:
            self.meteored_t = i.text
        
        print(f"Temperatura {self.meteored_t}")
        print("Estado: ",self.meteored_e)


    def accuweather(self):
        """ Retorna el estado y temperatura según el sitio Accuweather"""
        sopa = self._soup_validator(self._acuweather)
        temp_data = sopa.find_all('div',attrs={'class':'temp'})
        estado_data = sopa.find_all('div',attrs={'class':'phrase'})
        for t in temp_data:
            self.accuweather_t = t.text
            break

        for e in estado_data:
            self.accuweather_e = e.text
            break

        print(f"Temperatura {self.accuweather_t}")
        print("Estado: ",self.accuweather_e)

    def infoclima(self):
        """
        Retorna el estado y la temperatura según el sitio Info Clima.
        Utiliza la información de la URL de Info Clima para obtener el estado 
        y la temperatura actual, y muestra los resultados en la consola.

        Returns
        -------
        None
            No hay un valor de retorno específico.
        """
        sopa = self._soup_validator(self._infoclima)
        temp_data = sopa.find_all('div',attrs={'class':'d1'})
        estado_data = sopa.find_all('div',attrs={'d1'})
        
        for t in temp_data:
            if t.find('p') != None:
                sub = t.find('p').text
                self.infoClima_t = sub
                break
        for e in estado_data:
            self.infoClima_e = e.text.replace('\n','')
            break

        print(f"Temperatura {self.infoClima_t}")
        print("Estado: ",self.infoClima_e)


