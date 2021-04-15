import requests
from bs4 import BeautifulSoup

agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) ' \
        'Chrome/61.0.3163.100 Safari/537.36'
header = {'User-Agent': agent}


def img_fin(link):
    img_req = requests.get(url=link)
    img_pars = BeautifulSoup(img_req.text, "html.parser")
    a = open("non.html", "w", encoding="utf-8")
    b = "".join(str(img_pars.contents))
    a.write(b,)


url_image = "https://www.bing.com/images/search?view=detailV2&ccid=k5gv%2Bk5V&id=51EB8D7ECC14D523359693C3A878D7A63F1" \
            "ADC57&thid=OIP.k5gv-k5VxexBaa4XoknElAHaFj&mediaurl=https%3A%2F%2Fth.bing.com%2Fth%2Fid%2FR93982ffa4e55c5" \
            "ec4169ae17a249c494%3Frik%3DV9waP6bXeKjDkw%26riu%3Dhttp%253a%252f%252fdrwyjmricaxm7.cloudfront.net%252fre" \
            "pository%252fFrance-day-tours-and-excursions--On-The-Go-Tours-537101517504528_crop_800_600.jpg%26ehk%3D" \
            "hs0XqZausPJz90rRzUObyGO9eW29%252fVRK7z%252fg%252fa0COvY%253d%26risl%3D%26pid%3DImgRaw&exph=600&expw=800" \
            "&q=france&simid=608017857089599616&ck=5AD08DA36FBFCCE466BB3EA867DE9E72&selectedindex=35&form=IRPRST&vt=0&s" \
            "im=11"

print(img_fin(url_image))
