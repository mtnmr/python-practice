import json
from requests_oauthlib import OAuth1Session

CONSUMER_KEY = ''
CONSUMER_SECRET = ''
ACCESS_TOKEN = ''
ACCESS_TOKEN_SECRET = ''

#認証処理
twitter = OAuth1Session(CONSUMER_KEY,CONSUMER_SECRET,ACCESS_TOKEN,ACCESS_TOKEN_SECRET)

#自分の投稿（タイムライン）を取得してみる
url = 'twitter API探してコピーしてくる'
params = {'count':5}  #情報を何個取得するか

res = twitter.get(url, params=params)
res.status_code

timelines = json.loads(res.text)
timeline = timelines[0]
timeline['user']['description']

#ツイートしてみる
twitter = OAuth1Session(CONSUMER_KEY,CONSUMER_SECRET,ACCESS_TOKEN,ACCESS_TOKEN_SECRET)
url = '機能によって違うからまた探してくる'

params = {'status':'これはテストです'}

twitter.post(url, params=params)


