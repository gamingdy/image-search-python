# image-search-python
 

Ce projet a pour objectif de permettre la réalisation de recherche google image, le tout en console, ce qui permet par exemple d'effectuer une recherche d'image avec des bots 


#### Sommaires 

- [Installation](https://github.com/gamingdy/image-search-python/tree/dev/docs#installation)
- [Utilisation](https://github.com/gamingdy/image-search-python/tree/dev/docs#utilisation)
- [Bugs et Features](https://github.com/gamingdy/image-search-python/tree/dev/docs#bugs-et-features)


#### Installation

Pour installer le module vous pouvez simplement faire un ``pip install``


#### Utilisation

Maintenant le plus important, le module est enfin installer sur votre pc, il est maintenant temps de l'utilser.

Pour une simple recherche vous pouvez faire.

```py
from module_name import pony

img = pony("python langage")
# OU
img = pony(query="python langage")

print(img)      # Affiche une liste de un élément 

>>> ['https://cdn.futura-sciences.com/buildsv6/images/largeoriginal/3/9/a/39a7d35bbd_50163520_formation-python.jpg']
```

Si vous voulez spécifier le nombre de résultat vous pouvez faire

```py
from module_name import pony

img = pony("python langage", 5)
# OR
img = pony("python langage", num_result= 5)

print(img)

>>> # Affiche une liste avec cinq éléments
```

__**Attention**__: Le nombre max de résultats est de 20.


#### Bugs et features

Si vous rencontrez des bugs, vous pouvez créer un nouvelle issue avec des détails au sujet du bug rencontré.

Pour toute demandes de features vous pouvez créer un pull request, avec les détails sur la feature que vous aimeriez avoir