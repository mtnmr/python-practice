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
def pundh_out():
    worksheet = auth()
    df = pd.DateFrame(worksheet.get_all_records())

    timestamp = datetime.now
    punch_out = timestamp.strftime('%H:%M')

    df.iloc[-1,2] = [punch_out]
    worksheet.update([df.colums.values.tolist()] + df.values.tolist())
    print('退勤登録完了')


