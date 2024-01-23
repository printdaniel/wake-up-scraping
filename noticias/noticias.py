import requests 
from bs4 import BeautifulSoup 
from tabulate import tabulate
from base_parser import BaseParser

class Noticias(BaseParser):

    def __init__(self) -> None:
        self.pagina12 = 'https://www.pagina12.com.ar/secciones/el-pais'
        self.infbae = 'https://www.infobae.com/'


    def pagina(self):

        soup = self._soup_validator(self.pagina12)
        content_titulos = soup.find_all('a')

        for i in content_titulos:
            print(i.get_text())

    def info_bae(self):

        soup = self._soup_validator(self.infbae)
        content_titulos = soup.find_all('div', class_='story-card-info')
        for i in content_titulos:
            print(i.get_text())







