import requests
from bs4 import BeautifulSoup

class BaseParser:

    def _soup_validator(self, url, timeout=5, headers=None):
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
