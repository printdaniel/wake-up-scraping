import requests 
from bs4 import BeautifulSoup 
from tabulate import tabulate
from base_parser import BaseParser

class Noticias(BaseParser):

    def __init__(self) -> None:
        self.pagina12 = 'https://www.pagina12.com.ar/secciones/el-pais'


    def pagina(self):

        soup = self._soup_validator(self.pagina12)
        content_titulos = soup.find_all('a')

        for i in content_titulos:
            print(i.get_text())






