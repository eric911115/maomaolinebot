from importlib.resources import contents
import requests 
from bs4 import BeautifulSoup
import urllib.request as req
import json

url="https://www.fight30.com/products/mango-jump-towel"

with req.urlopen(url)as response:
    data=response.read().decode("utf-8")
 
root=BeautifulSoup(data,"html.parser")
titles=root.find("div",class_="out-of-stock txt-sold-out")
print(titles.text)