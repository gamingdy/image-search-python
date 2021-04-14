import requests
from bs4 import BeautifulSoup


recherche = input("Ta recherche : ")
recherche = recherche.replace(" ", "%20")
url = f"https://unsplash.com/s/photos/{recherche}"
print(url)
resp = requests.get(url)
soup = BeautifulSoup(resp.content, "html.parser")
print(soup)
