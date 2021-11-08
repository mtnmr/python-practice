import requests
import pandas as pd

REQUESR_URL = 'リクエストURLのうち不変の部分入れておく'
APP_ID = '自分のID'

params = {
    'format':'json',
    'large':'Japan',
    'small':'okinawa',
    'applicationid':APP_ID
    #入力パラメータの形に従う
}

res = requests.get(REQUESR_URL, params)
#RESPONSE[200]になれば成功
results = res.json()
#.jsonで中身が入れる

results['hotels'][0]['hotel'][0]['basicinfo']
#それぞれリスト形式に入っているからindexを指定すれば情報が取れる

#とってきた情報をpandasでデータフレーム形に変更したい
hotel_info = results['hotels'][0]['hotel'][0]['basicinfo']
pd.DataFrame(hotel_info, index=[0])  #何行目に入れるかindexで指定する

df = pd.DataFrame()
hotels = results['hotels']
for i, hotel in enumerate(hotels):
    hotel_info = hotel['hotel'][0]['basicinfo']
    _df = pd.DataFrame(hotel_info, index=[i])
    df = df.append(_df)

df.columns  #必要なカラムだけ取り出すために一旦全部のカラム名を取り出してみる

df[ ['hotelname', 'url', 'tel']].to_csv('hotel.csv', index=False, encoding='utf_8_sig') #encodingは文字化けしてる時に指定

