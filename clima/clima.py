import requests 
from bs4 import BeautifulSoup 
from base_parser import BaseParser

class Clima(BaseParser):
    def __init__(self) -> None:
        self._meteored = 'https://www.meteored.com.ar/tiempo-en_Federal-America+Sur-Argentina-Entre+Rios--1-16689.html'

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
