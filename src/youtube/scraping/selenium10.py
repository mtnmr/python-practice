#pip3 install -U selenium
#pip3 instakk webdriver_manager

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


#google chromeを自動で立ち上げ
browser = webdriver.Chrome(ChromeDriverManager().install())

#WEBページにアクセス
url = ''
browser.get(url)

#テキスト入力
elem_username = browser.find_element_by_id('username')
elem_username.send_keys('名前')

#ボタンクリック
login_btn = browser.find_element_by_id('login-btn')
login_btn.click()

#値の取得
elem_tbody = browser.find_elements_by_tag_name('tbody')
elems_th = elem_tbody.find_elements_by_tag_name('th')
elems_th[0].text

#プロパティの取得 href属性
elem_nav = browser.find_elements_by_id('nav_mobile')
elem_li = elem_nav.find_elements_by_tag_name('li')
elem_li[3].find_element_by_tag_name('a').get_attribute('href')

#CSSセレクタで要素を取得
browser.find_element_by_css_selector('#name').text

#XPATHで取得
browser.find_element_by_xpath('//[@id="name"]').text

#ページスクロール
browser.get(url)
browser.execute_script('window.scrollTo(0, 300);')
browser.execute_script('return document.body.scrollHeight')  #ページの高さを取得したいとき

browser.quit()  #ブラウザを閉じる

#ヘッドレスモードで立ち上げ
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument('--headless')

browser = webdriver.Chrome(ChromeDriverManager().install(), options=options)

#スクリーンショットを撮る
browser.get(url)

browser.set_window_size(1600, 1200)
browser.save_screenshot()
