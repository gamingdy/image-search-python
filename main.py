import requests
from bs4 import BeautifulSoup

agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) ' \
        'Chrome/61.0.3163.100 Safari/537.36'

header = {'User-Agent': agent}


def bing(query):
    query = query.replace(" ", "%20")
    url = f"https://www.bing.com/images/search?q={query}&form=HDRSC2&first=1&tsc=ImageBasicHover"
    rsp = requests.get(url, headers=header)
    soup = BeautifulSoup(rsp.text, "html.parser")
    a_balise = soup.find_all("a", {"class": "iusc"})
    bing = "https://www.bing.com"
    final_link = []
    for i in range(15):
        href = f"{a_balise[i]}"
        link_start = href.index("href=") + 6
        link_end = href.index("m='") - 3
        link = f"{bing}{href[link_start:link_end]}".replace("amp;", "")
        final_link.append(link)
    return "\n".join(final_link)





print(bing("france"))