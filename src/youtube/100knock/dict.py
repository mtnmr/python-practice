#要素の削除
dictionary = {
    'A' : 'kawai',
    'B' : 'mei',
    'C' : 'women',
    'D' : 'nagoya',
    'E' : 'travel'   
}

dictionary.pop('A')

dictionary.clear()

#情報の取得
dictionary.keys()

'men' in dictionary.values()

dictionary.items()

#要素の検索
dictionary['C']
dictionary.get('C')