# image-search-python

L'objectif de ce projet est d'effectuer des recherches google image avec python, le tout en console, ce qui permet par exemple d'effectuer une recherche d'image avec des bots

### Sommaires

- [Installation](https://github.com/gamingdy/image-search-python/tree/main/docs#installation)
- [Utilisation](https://github.com/gamingdy/image-search-python/tree/main/docs#utilisation)
- [Bugs et Features](https://github.com/gamingdy/image-search-python/tree/main/docs#bugs-et-features)


### Installation

Pour installer le module vous pouvez simplement faire un ``pip install imgsearch``.

[PIPY](https://pypi.org/project/imgsearch/)

### Utilisation

Maintenant le plus important, comment l'utiliser

Pour une simple recherche vous pouvez faire.

```py
from imgsearch import pony

img = pony("python langage")
# OU
img = pony(query="python langage")

print(img)      # Affiche une liste d'un élément 

>> ['https://cdn.futura-sciences.com/buildsv6/images/largeoriginal/3/9/a/39a7d35bbd_50163520_formation-python.jpg']
```

Si vous voulez spécifier le nombre de résultats vous pouvez faire

```py
from imgsearch import pony

img = pony("python langage", 5)
# OU
img = pony("python langage", num_result= 5)
# OU SINON
img = pony(query="python langage", num_result=5)

print(img)

>> # Affiche une liste avec cinq éléments
```

Si vous voulez des résultats random, vous pouvez faire

```py
from imgsearch import rainbow

img = rainbow("python langage", 5)
#OR 
img = rainbow(query="python langage", num_result=5)

print(img)

>> # Affiche une liste avec des résultat aléatoires, chaque fois
```

**🚨 Attention 🚨** : Le nombre max de résultats est de 20.


### Bugs et features

Si vous rencontrez des bugs, vous pouvez créer une issue avec des détails au sujet du bug rencontré.

Pour toute demandes de features vous pouvez créer un pull request, avec les détails sur la feature que vous aimeriez avoir
