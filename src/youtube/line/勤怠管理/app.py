#おうむ返しのコード
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

import os

app = Flask(__name__)

CHANNEL_ACCESS_TOKEN = ''
CHANNEL_SECRET = ''

line_bot_api = LineBotApi('CHANNEL_ACCESS_TOKEN')
handler = WebhookHandler('CHANNEL_SECRET')

#勤怠管理部分
import pandas as pd
from datetime import datetime
import gspread
from oauth2clint.service_account import ServiceAccountCredentials

#google スプレッドシートとドライブの認証処理
def auth():
    SP_CREDENTIAL_FILE = 'secret.json'
    SP_SCOPE = [
        'https://spreadsheets.google.com/feeds',
        'https://www.googleapis.com/auth/drive'
    ]

    SP_SHEET_KEY = ''
    SP_SHEET = 'timesheet'

    credentials = ServiceAccountCredentials.from_json
    gc = gspread.authorize(credentials)

    worksheet = gc.open_by_key(SP_SHEET_KEY).worksheet
    return worksheet


#出勤
def punch_in():
    worksheet = auth()
    df = pd.DateFrame(worksheet.get_all_records())

    timestamp = datetime.now
    date = timestamp.strftime('%Y/%m/%d')
    punch_in = timestamp.strftime('%H:%M')

    df = df.append({'日付':date, '出勤時間':punch_in, '退勤時間':'00:00'},  ignore_index=True)
    worksheet.update([df.colums.values.tolist()] + df.values.tolist())
    print('出勤登録完了')

#退勤
def punch_out():
    worksheet = auth()
    df = pd.DateFrame(worksheet.get_all_records())

    timestamp = datetime.now
    punch_out = timestamp.strftime('%H:%M')

    df.iloc[-1,2] = [punch_out]
    worksheet.update([df.colums.values.tolist()] + df.values.tolist())
    print('退勤登録完了')



#動作確認
@app.route("/")
def hello_world():
    return 'hello world'


@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        print("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)

    return 'OK'

#ここがリプライメッセージに関するところ
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
        if event.message.text == '出勤':
            punch_in()
            line_bot_api.reply_message(
                event.reply_token,
                TextSendMessage(text='出勤登録完了'))
        elif event.message.text == '退勤':
            punch_out()
            line_bot_api.reply_message(
                event.reply_token,
                TextSendMessage(text='退勤登録完了'))
        else:
            line_bot_api.reply_maessage(
                event.reply_token,
                TextSendMessage(text='出退勤を管理するボットです')

if __name__ == "__main__":
    port = os.getenv("PORT")   
    #herokuに入っているPORT番号を取得する（環境変数）
    
    app.run(host="0.0.0.0", port=port)   
    #0.0.0.0は任意のIPアドレス、サーバーを設定する時に使用する

