import json
from os import initgroups

#トークンとIDを保存したファイルを読み込む
file = open('/Users/kawaimei/Documents/GitHub/python-practice/src/youtube/line/info.json', 'r')
info = json.load(file)

from linebot import LineBotApi
from linebot.models import TextSendMessage

CHANNEL_ACCESS_TOKEN = info['CHANNEL_ACCESS_TOKEN']
line_bot_api = LineBotApi(CHANNEL_ACCESS_TOKEN)

def main():
    USER_ID = info['USER_ID']
    messages = TextSendMessage(text = 'おはよう')
    line_bot_api.push_message(USER_ID, messages)


if __name__ == '__main__':
    main()


#github actionsで定期実行
#ここからはjupyterlabのターミナルで実行
#git init                   初期化
#git remote add origin レポジトリのurl      紐付け
#git remote -v      urlが表示されればok
#git add .           .で全てを追加  
#git commit -m'1st commit'
#git push origin master
