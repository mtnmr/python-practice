import requests 
from bs4 import BeautifulSoup

url = 'https://scraping-for-beginner.herokuapp.com/ranking/'
res = requests.get(url)

soup = BeautifulSoup(res.text, 'html.parser')

#検証から、観光地の情報の1つの単位を見つける
spots = soup.find_all('div', attrs={'class':'u_areaListRankingBox'})

#まず1つの観光地名を取得
spot = spots[0]
spot.find_all('div', attrs={'class':'title'})  #find_allで思っている出力結果になってるか確認
spot_name = spot.find('div', attrs={'class':'title'})  #上記で1つしかなかったから、findを使う

spot_name.text   #'\n1観光地　1\n'が返ってくるので、観光地だけにしたい

spot_name.find('span', attrs={'class':'badge'}).extract()  #'\n観光地　1\n'になる
spot_name = spot_name.text.replace('\n', '')  #観光地　1'になる

#評点を取得
eval_num = spot.find('div', attrs={'class':'u_rankbox'})
eval_num = float(eval_num.text.replace('\n', ''))

#各カテゴリの評価を取得
categoryItems = spot.find('div', attrs={'class':'u_category'})  #各カテゴリに同じ構造で情報が入ってる

categoryItems = categoryItems.find_all('dl')
categoryItem = categoryItems[0] #1つ目のカテゴリが取れる

category = categoryItems.dt.text
rank = float(categoryItem.span.text)  #この２つを辞書形で取得

details = {}
for categoryItem in categoryItems:
    category = categoryItems.dt.text
    rank = float(categoryItem.span.text)

    details[category] = rank

#観光地名、評点、カテゴリ評価も合わせて辞書形に
datum = details
datum['観光地名'] = spot_name
datum['評点'] = eval_num 

#上記は観光地１つだったのを、for文で他の観光地情報も取得する
#これまでのコードまとめ

soup = BeautifulSoup(res.text, 'html.parser')

date = []  #全ての情報を格納する

spots = soup.find_all('div', attrs={'class':'u_areaListRankingBox'})
for spot in spots:
    spot_name = spot.find('div', attrs={'class':'title'}) 
    spot_name.find('span', attrs={'class':'badge'}).extract()
    spot_name = spot_name.text.replace('\n', '')

    eval_num = spot.find('div', attrs={'class':'u_rankbox'})
    eval_num = float(eval_num.text.replace('\n', ''))

    categoryItems = spot.find('div', attrs={'class':'u_category'})
    categoryItems = categoryItems.find_all('dl')

    details = {}
    for categoryItem in categoryItems:
        category = categoryItems.dt.text
        rank = float(categoryItem.span.text)

        details[category] = rank

    datum = details
    datum['観光地名'] = spot_name
    datum['評点'] = eval_num 

    date.append(datum)

#csvファイルにする
import pandas as pd
df = pd.DataFrame(date)

df.columns
df = df[['観光地名', '評点', 'アクセス', '楽しさ']]  #カラム名を並び替えれば、表の順番も変更できる

df.to_csv('観光地情報.csv', index=False)
