import pandas as pd

sr = pd.Series([1,2,3])

df = pd.DataFrame([
    [1,2,3],
    [4,5,6],
    [7,8,9]
])

#CSVファイルを読み込む
df = pd.read_csv('パス名')

df.head() #データの先頭をみる、デフォルトは５行、引数に何行か指定できる
df.tail() #データの後ろ５行
df[['longitude', 'latitude']] #ラベル名を指定して抽出
df.iloc[:,0:2]  #[行, 列]で取り出す部分を指定する
df.iloc[:, :-1] #最後の１行以外を取り出すならマイナスで指定もできる

df[df['ラベル名'] > 30]  #30より大きい値だけ取り出せる,中のかっこだけだとTrue,Falseで返すだけ

df.sort_values(by = 'ラベル名')

df.shape()
df.mean()
df.std()

df.values()  #numpyの形に変換（array）
