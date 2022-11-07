from importlib.resources import contents
import requests 
from bs4 import BeautifulSoup
import urllib.request as req
import time
import threading

def set_interval(func, sec):
    def func_wrapper():
        set_interval(func, sec)
        func()
    t = threading.Timer(sec, func_wrapper)
    t.start()
    return t

    
def mango():
    url="https://www.fight30.com/products/mango-jump-towel"
    
    with req.urlopen(url)as response:
        data=response.read().decode("utf-8")
 
    root=BeautifulSoup(data,"html.parser")
    titles=root.find("div",class_="out-of-stock txt-sold-out")
    if titles.text == "售完":
        
        return False
    
    
def DD():
    if mango()==False:
        print("YY")

set_interval(DD, 3)
    
    