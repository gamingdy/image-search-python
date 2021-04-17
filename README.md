# image-search-python
 
[Version française](https://github.com/gamingdy/image-search-python/tree/main/docs)


The objective of this project is to search an image on google with python, the whole in console, which allows, for example, a discord bot to search an image on google.


### Summary

- [Installation](https://github.com/gamingdy/image-search-python#installation)
- [Usage](https://github.com/gamingdy/image-search-python#usage)
- [Bugs and Feature](https://github.com/gamingdy/image-search-python#bugsfeatures)


### Installation

For install you can simply do  ``pip install module_name`` 


### Usage

Now the most important thing, how to use it

For a simple search, you can do this.

```py
from imgsearch import pony

img = pony("python langage")
# OR
img = pony(query="python langage")

print(img)      # Print a list with one element

>> ['https://cdn.futura-sciences.com/buildsv6/images/largeoriginal/3/9/a/39a7d35bbd_50163520_formation-python.jpg']
```

If you want to specify the results' number, you can do

```py
from imgsearch import pony

img = pony("python langage", 5)
# OR
img = pony("python langage", num_result= 5)
#OR ELSE
img = pony(query="python langage", num_result=5)

print(img)

>> # Print a list with five elements
```

**🚨 Warning 🚨**: The max value of results is 20 


### Bugs/Features

If you encounter a bug, you can create an issue, with details of the bug encountered.

For more features, you can create a pull request, with details about your features
