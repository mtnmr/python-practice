#ファイル操作の基本
file = open('sample.txt')
text = file.read()
file.close()

#テキストデータをwith構文を使って取得
with open('sample.txt', 'r') as f:
    text = f.read()

#jsonファイル
import json
with open('sanple.json', 'r') as f:
    date = json.load(f)

date['store name']
