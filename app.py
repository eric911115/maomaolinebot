from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)

from importlib.resources import contents
import requests 
from bs4 import BeautifulSoup
from urllib.request import urlretrieve 
import requests.packages.urllib3
import urllib.request as req
requests.packages.urllib3.disable_warnings()
import threading
gg=0
app = Flask(__name__)

line_bot_api = LineBotApi('zegN/VBfBTlX9qAQoGJWWMazAUWyEN/DI+kPR+lqIaoWTamaIZq59REhdduCL1n+tQsjHPrWXpMckk+gOGON/coXA9Bx47cVJoDxBbeA3fLlxA3TwdYW/u9yPM3IWm0NoMoE1I4hfXDC+OR0viORlwdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('f7daa972ca14bb6c060aec3245beb7e9')

@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    print("Request body: " + body, "Signature: " + signature)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'



def movie():
    target_url = 'https://movies.yahoo.com.tw/movie_intheaters.html'
    rs = requests.session()
    res = rs.get(target_url, verify=False)
    res.encoding = 'utf-8'
    soup = BeautifulSoup(res.text, 'html.parser')   
    content = ""
    for index, data in enumerate(soup.select('div.release_movie_name a')):
        if index == 20:
            return content       
        title = data.text
        content += '{}\n'.format(title).lstrip()
    return content

def mango():
    url="https://www.fight30.com/products/mango-jump-towel"

    with req.urlopen(url)as response:
        data=response.read().decode("utf-8")
 
    root=BeautifulSoup(data,"html.parser")
    titles=root.find("div",class_="out-of-stock txt-sold-out")
    if titles.text == "售完":
        return False
    


@handler.add(MessageEvent, message=TextMessage)
def set_interval(func, sec):
    def func_wrapper():
        set_interval(func, sec)
        func()
    t = threading.Timer(sec, func_wrapper)
    t.start()
    return t
def DD():
    if(mango)==False:  
        line_bot_api.push_message('Uadeefb1e5194071cb79756915b8b5309', TextSendMessage(text='Hello World!'))
        
def handle_message(event):
    if gg == 1:
        #print("Handle: reply_token: " + event.reply_token + ", message: " + event.message.text)
        content = movie()
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=content))
    elif mango() == True:
        #print("Handle: reply_token: " + event.reply_token + ", message: " + event.message.text)
        content = "https://www.fight30.com/products/mango-jump-towel"
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=content))
    else:
        content = "{}".format(event.message.text)
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=content))
set_interval(DD, 3)
import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 80))
    app.run(host='0.0.0.0', port=port)
