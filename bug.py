from importlib.resources import contents
import requests 
from bs4 import BeautifulSoup
import urllib.request as req
import json



target_url = 'https://movies.yahoo.com.tw/movie_intheaters.html'
rs = requests.session()
res = rs.get(target_url, verify=False)
res.encoding = 'utf-8'
print(res)
soup = BeautifulSoup(res.text, 'html.parser')   
content = ""
data =soup.find("div",class_="out-of-stock txt-sold-out")     

