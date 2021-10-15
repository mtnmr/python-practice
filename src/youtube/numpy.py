#外部ライブラリなのでインストール必要
import numpy as np

x = np.array([1,2,3])
x.shape #(3,)
x.ndim  #1

y = np.array([
    [1,2,3],
    [4,5,6],
    [7,8,9]
])
y.shape  #(3,3)
y.ndim  #2

np.zeros((2,2))  #2*2の中身が0の行列を作る

y.mean()  #中の数字の平均をとる
y.mean(axis = 1) # 横１行の平均をとる
y.var()
y.std()
y.max()

X = np.array([
    [2,3],
    [1,5],
    [3,1]
])

X.T  #転置
#array([2,1,3],
#      [3,5,1])  行、列を逆にする

np.dot(X, X.T)  #行列の積

