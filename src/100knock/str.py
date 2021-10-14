#文字列

name = 'Mei'
area = 'gihu'

print(f'私は{name}です。{area}出身です。')

#エスケープシーケンス
print('いつもの帰り道とは違うルートで帰ってみようかな。\n迷子にならないか心配だけど。')

#書式化
print('10進数=%d,　16進数=%x,　10進浮動小数点数=%f' % (16,16,16))


#大文字、小文字
print('hello'.upper())
print('WORLD'.lower())

#文字列分割
message = 'こんにちは。\n私はAIのロボットです。'
message.split('\n')

#文字列の結合
messages = message.split('\n')
''.join(messages)

#空白除去
message = '　いつも食べるここのケーキはとても美味しいね。　'
message.strip()

#文字列の置換
message = '今日は晴れですね。'
message.replace('晴れ', '雨')

#文字列検索
message = '今日はとても夜空が綺麗だ。'
message.find('夜空')

#型変換
x = 1
str(x)

x = 1.52
str(x)

x = [1, 2, 3]
str(x)

x = dict(name='john', birth='US')
str(x)

#包含関係
A, B = 'sba', 'gasba'
print(A in B)

A, B = 'xdh', 'orweit'
print(A in B)

