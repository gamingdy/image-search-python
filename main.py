from requests import get
from bs4 import BeautifulSoup

agent = "Mozilla/5.0 (Linux; U; Android 2.3.3; fr-fr; GT-I9100 Build/GINGERBREAD) AppleWebKit/533.1 " \
        "(KHTML, like Gecko) Version/4.0 Mobile Safari/533.1"

header = {'User-Agent': agent}


def pony(query, num_result=1):
    img_search = query.replace(" ", "+")
    url = f"https://google.com/search?q={img_search}&source=lnms&tbm=isch"
    r = get(url, headers=header)
    soup = BeautifulSoup(r.text, "html.parser")
    a_div = soup.find_all("div", {"class": "lIMUZd"})
    img_link = []
    if num_result > len(a_div):
        result = len(a_div)
    else:
        result = num_result
    for i in range(len(a_div)):
        a_balise = f"{a_div[i]}"
        if ' class="BhZo9">' in a_balise:
            pass
        elif a_balise.startswith('<div class="lIMUZd"><div><table class="By0U9">'):
            pass
        else:
            src_start = a_balise.index('imgurl=') + 7
            src_end = a_balise.index('imgrefurl') - 5
            img_link.append(f"{a_balise[src_start:src_end]}")
    return img_link[0:result]

print(pony("pygame"))