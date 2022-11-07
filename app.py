from importlib.resources import contents
import requests 
from bs4 import BeautifulSoup
import urllib.request as req
import time
import random
import os
i=0
# def set_interval(func, sec):
#     def func_wrapper():
#         set_interval(func, sec)
#         func()
#     t = threading.Timer(sec, func_wrapper)
#     t.start()
#     return t
# global r

def mango():
    url="https://www.fight30.com/products/mango-jump-towel"
    request=req.Request(url,headers={
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36"
    })    
    with req.urlopen(url)as response:
        data=response.read().decode("utf-8")
    root=BeautifulSoup(data,"html.parser")
    titles=root.find("div",class_="out-of-stock txt-sold-out")
    if titles.text != "售完":
        headers = {
            "Authorization": "Bearer " + "PGJPHdnyMzzNkxpzVzPK90z2KZ1K6kg0OLqbtWTTFqn",
            "Content-Type": "application/x-www-form-urlencoded"
        }
        params = {"message":"芒果醬毛巾有貨了 速速購買\nhttps://www.fight30.com/products/mango-jump-towel"}
        r = requests.post("https://notify-api.line.me/api/notify",
                        headers=headers, params=params)
        print(r.status_code)  #200

def VH():
    url="https://www.fight30.com/products/vh-t-g-b-towel"
    request=req.Request(url,headers={
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36"
    })
    with req.urlopen(url)as response:
        data=response.read().decode("utf-8")
    
    root=BeautifulSoup(data,"html.parser")
    titles=root.find("div",class_="out-of-stock txt-sold-out")
    if titles.text != "售完":
        headers = {
            "Authorization": "Bearer " + "PGJPHdnyMzzNkxpzVzPK90z2KZ1K6kg0OLqbtWTTFqn",
            "Content-Type": "application/x-www-form-urlencoded"
        }
        params = {"message":"VH毛巾有貨了 速速購買\nhttps://www.fight30.com/products/vh-t-g-b-towel"}
        r = requests.post("https://notify-api.line.me/api/notify",
                        headers=headers, params=params)
        print(r.status_code)  #200
while(i<10):
    mango()
    i=1
    print(i)
    time.sleep(random.uniform(6, 10))
    i=2
    print(i)
    VH()
    i=3
    print(i)

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 80))
    app.run(host='0.0.0.0', port=port)