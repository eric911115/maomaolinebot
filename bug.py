from importlib.resources import contents
import requests 
from bs4 import BeautifulSoup
from urllib.request import urlretrieve 
import requests.packages.urllib3
requests.packages.urllib3.disable_warnings()


    
target_url = 'https://www.fight30.com/products/mango-jump-towel'
rs = requests.session()
res = rs.get(target_url, verify=False)
res.encoding = 'utf-8'
soup = BeautifulSoup(res.text, 'html.parser')   
content = ""
for index, data in enumerate(soup.select('div.out-of-stock txt-sold-out')):
    if index == 20:      
        title = data.text
        content += '{}\n'.format(title).lstrip()
    print(content)
