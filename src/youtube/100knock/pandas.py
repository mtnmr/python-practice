import collections
from decimal import DivisionUndefined
import pandas as pd

#データ読み込み
df = pd.read_csv('wether.csv')

#内容確認
df.head(3)
df.rail(10)

#不要な行や列の削除
df.columns  #カラム名を全部取り出してみる,取り出したカラム名からいらないカラムを消してdfに入れる
df = df[['カラム名',
'カラム名２',
'カラム名３'
]][1:]

#データフレームに関する情報取得
df.dtypes
df.shape
df.columns
df.index

#任意の要素を取得
df.iloc[4:10, 2:6]

#条件抽出
df_people = pd.read_csv('people.csv')
df_people[df_people['nationality'] == 'America']
df_people.query('nationality == "America" ')

df_people[(df_people['age'] >= 20) and (df_people['age'] < 30)]
df_people.query('age >=20 & age < 30')

#カラムごとのユニークな値を抽出
df_people['nationality'].unique()

#重複除去
df_people.drop_duplicates(subset='nationality')

#カラム名の変更
df.columns = ['新しいカラム名']
df.rename(columns={
    'old':'new',
    'old2':'new2',
    'old3':'new3'
})

#並び替え
df.sort_values('カラム名', ascending=False)

#ダミーデータへの処理
df_people['nationality'].unique()
pd.get_dummies(df_people, columns=['nationality'])

#欠損値の確認、補完
df.isnull()
df.fillna(0)
df.dropna(axis=1)

#ユニークな値と出現回数
df_iris = pd.read_csv('iris.csv')
df_iris['Class'].value_counts()

#グループごとの集計（それぞれの平均値）
df_iris.groupby('Class').mean()

#統計量の確認
df.mean()
df.median()
df.std()
df.max()
df.min()

#グラフ表示
import matplotlib.pyplot as plt
df[:50].plot(x='年月日', y=['平均気温','最高気温','最低気温'], legend=False)

#相関係数を算出
df[['項目１', '項目２', '項目３']].corr()

#データの出力
df.fillna(0).to_csv('export.csv', index=False)

