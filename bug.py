from importlib.resources import contents
import requests 
from bs4 import BeautifulSoup
import urllib.request as req
import time
def setInterval(func, sec):
    time.sleep(sec)
    func()
    setInterval(func(), sec)

    setInterval(mango, 10)
def mango():
    url="https://www.fight30.com/products/mango-jump-towel"

    with req.urlopen(url)as response:
        data=response.read().decode("utf-8")
 
    root=BeautifulSoup(data,"html.parser")
    titles=root.find("div",class_="out-of-stock txt-sold-out")
    if titles.text == "售完":
        return False

if mango()==True:
    print("u")
else:
    print("dd")
    
    