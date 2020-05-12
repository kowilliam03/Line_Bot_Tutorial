from flask import Flask, request, abort

from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage

from configparser import ConfigParser

from getStockPrice import get_stock_price

app = Flask(__name__)

# read config.ini
config = ConfigParser()
config.read('config.ini')

line_bot_api = LineBotApi(config['LINE']['ACCESS_TOKEN'])
handler = WebhookHandler(config['LINE']['CHANNEL_SECRET'])


@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info('Request body: ' + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        print('Invalid signature. Please check your channel access token/channel secret.')
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    def send_message(token, content):
        line_bot_api.reply_message(
            token,
            TextMessage(text=content)
        )

    stocks = {
        "3008": "大立光",
        "2330": "臺積電",
        "1216": "統一"
    }

    text = event.message.text
    message = ""
    if text in stocks:
        stock_price = get_stock_price(text)
        message = f"{text} {stocks[text]} 目前股價爲: {stock_price}"
    else:
        message = "請輸入要查詢的股票代號：(1216 統一, 2330 臺積電, 3008 大立光)"

    send_message(event.reply_token, message)

if __name__ == "__main__":
    app.run()
