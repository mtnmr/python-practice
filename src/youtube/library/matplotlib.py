import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('パス名sample_date.csv')

#散布図(データの関係性をみる)
plt.scatter(df['tate'], df['yoko'])

#ヒストグラム（データの散らばりをみる、どの値がどれくらいあるか）
plt.hist(df['ラベル名'])
plt.hist(df['ラベル名'], bins = 20)  #binsで何分割して分布をみるか指定できる

#折線グラフ
import numpy as np
x = np.linspace(1, 100, 100)  #1-100までの数値を100分割する
y = 2 * x
plt.plot(x, y)
