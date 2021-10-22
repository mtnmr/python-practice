import numpy as np

#ベクトル定義
a = np.array([1,2,3,4])
a.shape

#行列の定義
b = np.array([1,2], [3,4])

#要素数８のゼロベクトル
c = np.zeros(8)

#(4,3)のゼロ行列
d = np.zeros((4,3))

#単位行列
np.eye(5)

#加減乗除
A = np.aarray([1,5], [4,-2])
B = np.array([2,-1], [7,6])
A + B
A - B
np.dot(A, B)

#統計計算
A = np.array([1,5,-2], [4,0,-3], [-8,2,6])
A.sum()
A.max()
A.min()
np.average(A)
np.median(A)
np.var(A)
np.std(A)

#行列式と逆行列
A = np.array([1,5], [4,-3])
a = np.linalg.det(A)  #行列式の計算結果、０でなければ逆行列が存在
A_inv = np.linalg.inv(A)
np.dot(A, A_inv)  #単位行列になってるか確認
