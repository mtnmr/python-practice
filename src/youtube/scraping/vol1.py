import selenium

#!brew install choromedriver(google chorome を起動するために必要)

from selenium import webdriver
from time import sleep

#ブラウザを起動する
browser = webdriver.Chrome()  #これでchoromeを起動できる

#ブラウザを止めるとき
browser.quit()

#ブラウザにアクセスする
url = 'https://scraping-for-beginner.herokuapp.com/login_page'
browser.get('url')

sleep(4)

#ログインページにusername,passを入力
elem_username = browser.find_element_by_id('username')
elem_username.send_keys('imanishi')

elem_password = browser.find_element_by_id('password')
elem_password.send_keys('kohei')


sleep(1)

#ログインボタンをおす
elem_login = browser.find_element_by_id('login-btn')
elem_login.click()

#ヘッドレスモード
from selenium.webdriver.chrome.options import Options
options = Options()
options.add_argument('--headless')
browser = webdriver.Chrome(options=options)
url = ''
browser.get(url)
