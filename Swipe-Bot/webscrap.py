import requests
from colorama import Fore, Style, init
from bs4 import BeautifulSoup

# Inicializa colorama
init(autoreset=True)

sitio_web = "https://badoo.com/es/"
resultado = requests.get(sitio_web)
contenido = resultado.text

# Imprimir todo el contenido HTML
print(Fore.GREEN + contenido)

# Usar BeautifulSoup para encontrar todos los enlaces en la página
soup = BeautifulSoup(contenido, 'html.parser')
enlaces = soup.find_all('a')

# Imprime todos los enlaces encontrados
for enlace in enlaces:
    print(Fore.YELLOW + str(enlace.get('href')))
