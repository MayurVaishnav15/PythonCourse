""" Two types of modules 
    Internal modules
    External modules

    https://docs.python.org/3/py-modindex.html
"""

import math
import mymodule
import requests


print(math.sqrt(9))
mymodule.hello()
r = requests.get("https://www.netflix.com")
print(r.text)