import datetime

#現在の日時の取得
datetime.datetime.now()

#現在の日付を取得
datetime.date.today()

#任意の日付を取得
datetime.date(2021, 1, 1)
 
#日時の各情報を取得
now = datetime.datetime.now()
now.year
now.month
now.day
now.hour
now.minute
now.second
now.strftime('%A')

#日付計算
from datetime import timedelta
today = datetime.date.today()
today - timedelta(days=2)

#日付比較
datetime.date(2020, 1, 1) < datetime(2021, 1, 1)

#フォーマット変換
today = datetime.date.today()
today.strftime('%Y/%M/%D')
 