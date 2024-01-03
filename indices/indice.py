import requests 
from bs4 import BeautifulSoup 


dolarito = requests.get('https://www.dolarito.ar/')

htmlData = dolarito.content

parserData = BeautifulSoup(htmlData, "html.parser")


print(htmlData)
print(parserData.prettify())
