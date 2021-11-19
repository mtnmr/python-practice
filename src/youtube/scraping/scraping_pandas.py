from collections import UserList
import pandas as pd

url = 'https://info.finance.yahoo.co.jp/ranking/?kd=1&tm=d&mk=1'
dfs = pd.read_html(url)

len(dfs)  #１が返ってくる、表の数

df = dfs[0]
df.head()  #数字でも文字列で保存されてしまうから、後処理をする
df.tail()  #先頭と末尾のデータだけでもみて確認してみる

df = df.drop(df.index[-1])  #最後の行削除

df['順位'].dtype  #データ型をかくにん
df = df.astype({'順位':int})

df['増加値'] = [datum.replace('+', '') for datum in df['増加値'].tolist()]

df = df.astype(
    {'順位':int,
    'コード':int,
    '増加値':int,
    '取引値':int
    })

df['前日比'] = [datum.replace('+', '').replace('%','') for datum in df['前日比'].tolist()]
df = df.astype({'前日比':float})

import datetime
now = datetime.datetime.now()
year = now.year
month = now.month
day = now.day
date = datetime.date(year, month, day)
df['日付'] = [date]*len(df)

