import requests
from bs4 import BeautifulSoup


header={'User-Agent': "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.1"
                      "34 Safari/537.36"}


def imgsearch(search, result_number=1):
    query = search.replace(' ', '+')
    result = result_number
    url = f"https://google.com/search?q={query}&source=lnms&tbm=isch"
    print(url)
    resp = requests.get(url, headers=header)
    soup = BeautifulSoup(resp.content, "html.parser")
    print(soup)



imgsearch("usa", 10)
