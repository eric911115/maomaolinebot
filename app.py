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


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    #print("Handle: reply_token: " + event.reply_token + ", message: " + event.message.text)
    content = "{}: {}".format(event.source.user_id, event.message.text)
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=content))

import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 80))
    app.run(host='0.0.0.0', port=port)
