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

from linebot.models import *

import requests 
from bs4 import BeautifulSoup
from urllib.request import urlretrieve 

app = Flask(__name__)


line_bot_api = LineBotApi('zegN/VBfBTlX9qAQoGJWWMazAUWyEN/DI+kPR+lqIaoWTamaIZq59REhdduCL1n+tQsjHPrWXpMckk+gOGON/coXA9Bx47cVJoDxBbeA3fLlxA3TwdYW/u9yPM3IWm0NoMoE1I4hfXDC+OR0viORlwdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('f7daa972ca14bb6c060aec3245beb7e9')

@app.route("/", methods=['GET'])
def hello():
    return "Hello World!"

@app.route("/", methods=['POST'])
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


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    msg = event.message.text
    print(msg)
    msg = msg.encode('utf-8')
    if event.message.text == "最新電影":
        a=movie()
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text=a))

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
        title = data.text.lstrip().rstrip()
        content += '{}\n'.format(title)
    return content

if __name__ == "__main__":
    app.run(debug=True,port=80)