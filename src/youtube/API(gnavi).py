import requests

url = 'APIに表示されたurl'

params = {}
params['keyid'] = '必須項目：登録時に届いたアクセスキー'
params['freeword'] = '神田駅,肉'

response = requests.get(url, params)

import pprint
pprint.pprint(response.json())

results = response.json()

restrants = results['rest']
restrants[0]['name']
restrants[-1]['url']

