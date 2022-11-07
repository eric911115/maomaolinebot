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

    

url="https://www.fight30.com/products/mango-jump-towel"
    
with req.urlopen(url)as response:
    data=response.read().decode("utf-8")
 
root=BeautifulSoup(data,"html.parser")
titles=root.find("div",class_="out-of-stock txt-sold-out")
if titles.text == "售完":
    headers = {
        "Authorization": "Bearer " + "NpxGoV7UPJ0GT0jRWChIvVuqg6hKJU7QTms3vCW6i64",
        "Content-Type": "application/x-www-form-urlencoded"
    }
    params = {"message":"芒果醬毛巾有貨了 速速購買\nhttps://www.fight30.com/products/mango-jump-towel"}
    r = requests.post("https://notify-api.line.me/api/notify",
                      headers=headers, params=params)
    print(r.status_code)  #200
  