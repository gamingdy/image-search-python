import requests
from bs4 import BeautifulSoup

agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) ' \
        'Chrome/61.0.3163.100 Safari/537.36'
header = {'User-Agent': agent}


def img_fin(link):
    img_req = requests.get(url=link)
    img_pars = BeautifulSoup(img_req.text, "html.parser")
    print(img_pars)


url_image = "https://www.bing.com/images/search?view=detailV2&ccid=s%2bOYui1H&id=2BFF496C57BF963630DB68300AE193053C8" \
            "C12F5&thid=OIP.s-OYui1H2TGvEPfuAl-QfQHaKX&mediaurl=https%3a%2f%2fth.bing.com%2fth%2fid%2fRb3e398ba2d47d" \
            "931af10f7ee025f907d%3frik%3d9RKMPAWT4QowaA%26riu%3dhttp%253a%252f%252fsparkhistory.com%252fwp-content%2" \
            "52fuploads%252f2018%252f04%252fparis-france-eiffel-tower-roadview-SparkHistory.jpg%26ehk%3dc9O261A3tce" \
            "p3IivpPVLOBxOdhW4fE4W3yhSMZR4Jxw%253d%26risl%3d%26pid%3dImgRaw&exph=3673&expw=2624&q=france&simid=6080" \
            "36445704451443&ck=D4DE5E1E599D3E0A37B1F8B442867B81&selectedIndex=0&FORM=IRPRS"

print(url_image)


url = "https://www.bing.com/images/search?q=france&form=HDRSC2&first=1&tsc=ImageBasicHover"
rsp = requests.get(url, headers=header)
soup = BeautifulSoup(rsp.text, "html.parser")
a_balise = soup.find_all("a", {"class": "iusc"})
link = []
bing = "https://www.bing.com"

for i in range(15):
    href = f"{a_balise[i]}"
    link_start = href.index("href=")+6
    link_end = href.index("m='")-3
    link = f"{bing}{href[link_start:link_end]}".replace("amp;", "")
    print(link)
