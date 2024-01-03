import requests 
from bs4 import BeautifulSoup 

def soup(URL):
    page = requests.get(URL)
    soup = BeautifulSoup(page.value,"html.parser")
    return soup


soup = soup('https://www.cronista.com/')
value = soup.find_all('span', attrs={'class':'value'})


for i in value:
    print(i.text)
