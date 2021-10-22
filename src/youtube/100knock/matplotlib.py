import matplotlib.pyplot as plt

#折線グラフ
import numpy as np
data = np.random.randit(0, 100, size=(50,2))
plt.plot(data)

#散布図
data = np.random.randit(0, 50, size=(2,100))
plt.scatter(*data)

#棒グラフ
x = [1,2,3,4,5]
data = np.random.randit(0, 100, size=(5,))
labels = ['Math','Phisics','Chemistory','English','History']
plt.bar(x, data, ticl_label=labels)  #縦の棒グラフ
plt.barh(x, data, ticl_label=labels)  #横の棒グラフ

#ヒストグラム
data = np.random.randit(0, 100, size=(20,))
plt.hist(data, bins=5) 

#タイトルと凡例,軸の名前と範囲指定, マーカーの色設定・種類設定
male_ht = np.random.randit(150, 200, size=(50,))
male_wt = np.random.randit(50, 110, size=(50,))
female_ht = np.random.randit(130, 170, size=(50,))
female_wt = np.random.randit(30, 80, size=(50,))

plt.scatter(male_ht, male_wt, label='male')
plt.scatter(female_ht, female_wt, label='female')

plt.title('Height amd Weight')
plt.legend()

plt.xlabel('Height[cm]')
plt.ylabel('Weight[kg]')

plt.xlim(110, 210)
plt.ylim(20, 120)

plt.scatter(male_ht, male_wt, label='male', color='skyblue')
plt.scatter(female_ht, female_wt, label='female', color='pink')

plt.scatter(male_ht, male_wt, label='male', marker='>')  #マーカーは▷
plt.scatter(female_ht, female_wt, label='female', marker='<')  #マーカーは◁

#グラフを画像ファイルで出力
data = np.dandpm.randit(0, 100, size=(50,2))
plt.plot(data)
plt.savefig('sample.png')
