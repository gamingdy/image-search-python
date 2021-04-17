# image-search-python
 

[Version française](https://github.com/gamingdy/image-search-python/tree/dev/docs)


The objective of this project is to make a search with google image, the whole in console, that's allow for a exemple , a bot who can made an image search on google.


#### Summary

- [Installation](https://github.com/gamingdy/image-search-python#installation)
- [Usage](https://github.com/gamingdy/image-search-python#usage)
- [Bugs and Feature](https://github.com/gamingdy/image-search-python#bugsfeatures)
#### Installation

For install you can simply do  ``pip install module_name`` 

#### Usage

Now, the most important thing. You have module on your computer and it's time to use it.

For a simply search, you must do this

```py
from module_name import pony

img = pony("python")
# OR
img = pony(query="python")

print(img)      # Print a list with one element

>>> ['https://cdn.futura-sciences.com/buildsv6/images/largeoriginal/3/9/a/39a7d35bbd_50163520_formation-python.jpg']
```

If you want specify number of result you can do

```py
from module_name import pony

img = pony("python langage", 5)
# OR
img = pony("python langage", num_result= 5)

print(img)

>>> # Print a list with five elements
```

#### Bugs/Features

If you encounter a bug, you can create an issue, with details of the bug encountered.

For features you can create a pull request, with details about your features