#pip3 install helium

from helium import *

#立ち上げ
driver = start_chrome('url', headless=True)

#クリック
click('ログイン')  #表示されているテキストを書けばいい

#ログイン画面
write('入れたい名前', into='Enter user name（入力したい箇所に書いてある）')
write('入れたいパスワード', into='Enter your password')
click('LOGIN')

#要素取得
_items = find_all(S('th'))
items = [_item.web_element.text  for _item in _items]
#'th'のラグをとって中の文字だけ取れる

#スクリーンショット
get_driver().save_screenshot('scrennshot.png')





