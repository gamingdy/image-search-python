import requests
from bs4 import BeautifulSoup

agent = "Mozilla/5.0 (Linux; U; Android 2.3.3; fr-fr; GT-I9100 Build/GINGERBREAD) AppleWebKit/533.1 " \
        "(KHTML, like Gecko) Version/4.0 Mobile Safari/533.1"
header = {'User-Agent': agent}

img_search = input("recheche: ")
img_search = img_search.replace(" ", "+")
url = f"https://google.com/search?q={img_search}&source=lnms&tbm=isch"
r = requests.get(url, headers=header)
soup = BeautifulSoup(r.text, "html.parser")
a_div = soup.find_all("div", {"class": "lIMUZd"})
google_link = "https://www.google.com"

for i in range(len(a_div)):
    a_balise = f"{a_div[i]}"
    if ' class="BhZo9">' in a_balise:
        pass
    elif a_balise.startswith('<div class="lIMUZd"><div><table class="By0U9">'):
        pass
    else:
        src_start = a_balise.index('imgurl=') + 7
        src_end = a_balise.index('imgrefurl') - 5
        print(f"{a_balise[src_start:src_end]}")

def rainbow():
    print("nom de la fonction pour les resultat random")