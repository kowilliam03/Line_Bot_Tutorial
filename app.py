from flask import Flask, request, abort

from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage, ImageSendMessage

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
    def send_message(token, message):
        line_bot_api.reply_message(
            token,
            message
            # TextMessage(text=content)
        )

    stocks = {
        "3008": "大立光",
        "2330": "臺積電",
        "1216": "統一"
    }

    text = event.message.text
    if text in stocks:
        stock_price = get_stock_price(text)
        content = f"{text} {stocks[text]} 目前股價爲: {stock_price}"
    else:
        content = "請輸入要查詢的股票代號：(1216 統一, 2330 臺積電, 3008 大立光)"

    # send_message(event.reply_token, TextMessage(text=content))
    image_url = "https://i.imgur.com/TeoVsOc.png"
    send_message(event.reply_token, ImageSendMessage(
        original_content_url=image_url,
        preview_image_url=image_url
    ))


if __name__ == "__main__":
    app.run()
