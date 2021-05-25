from requests import get
from bs4 import BeautifulSoup
from random import sample

agent = "Mozilla/5.0 (Linux; U; Android 2.3.3; fr-fr; GT-I9100 Build/GINGERBREAD) AppleWebKit/533.1 " \
        "(KHTML, like Gecko) Version/4.0 Mobile Safari/533.1"

header = {'User-Agent': agent}

list_img_type = {
    "gif": "tbm=isch&tbs=itp:animated",
    "wb": "tbm=isch&tbs=ic:gray",
    "all": "tbm=isch"
}


def pony(query, num_result=1, img_type="all"):
    """
    Search on google image

    :param query: --> Your request
    :param num_result: --> Number of result, the max value is 20
    :param img_type: --> Type of image, they are 3 type of image:("all" : return all image type
                                                                  "gif": return only gif image
                                                                  "wb": return only white and black image)                                                  
    """
    img_search = str(query).replace(" ", "+")
    type_of_img = list_img_type[img_type] if img_type in list_img_type.keys() else list_img_type["all"]
    url = f"https://google.com/search?q={img_search}&source=lnms&{type_of_img}"
    r = get(url, headers=header)
    a_div = BeautifulSoup(r.text, "html.parser").find_all("div", {"class": "lIMUZd"})
    img_link = []
    result = len(a_div) if num_result > len(a_div) else num_result

    for i in range(result):
        a_balise = f"{a_div[i]}"
        if ' class="BhZo9">' not in a_balise or a_balise.startswith('<div class="lIMUZd"><div><table class="By0U9">'):
            src_start = a_balise.index('imgurl=') + 7
            src_end = a_balise.index('imgrefurl') - 5
            img_link.append(f"{a_balise[src_start:src_end]}")

    return img_link


def rainbow(query, num_result=1, img_type="all"):
    """
    Search on google image and return random image each time

    :param query: --> Your request
    :param num_result: --> Number of result, the max value is 20
    :param img_type: --> Type of image, they are 3 type of image, by default value is "all":("all" : return all image type
                                                                                             "gif": return only gif image
                                                                                             "wb": return only white and black image)                                                 
    """
    req = pony(query, 20,img_type)
    result = len(req) if num_result > len(req) else num_result
    return sample(req, k=result)


print(pony("python", img_type="wb"))