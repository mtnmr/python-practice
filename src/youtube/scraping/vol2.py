from selenium import webdriver

browser = webdriver.Chrome()
browser.get('https://scraping-for-beginner.herokuapp.com/login_page')

elem_username = browser.find_element_by_id('username')
elem_username.send_keys('imanishi')

elem_password = browser.find_element_by_id('password')
elem_password.send_keys('kohei')

elem_login = browser.find_element_by_id('login-btn')
elem_login.click()

#テキスト取得
elem = browser.find_element_by_id('name')
name = elem.text

elem = browser.find_element_by_id('company')
company = elem.text

elem = browser.find_element_by_id('birthday')
birthday = elem.text

elem = browser.find_element_by_id('hobby')
hobby = elem.text
hobby.replace('\n', '.')

#まとめて取得
elems_th = browser.find_elements_by_tag_name('th')

keys = []
for elem_th in elems_th:
    key = elem_th.text
    keys.append(key)

elems_td = browser.find_elements_by_tag_name('td')
values = []
for elem_th in elems_td:
    value = elem_th.text
    values.append(key)

#csvに出力
import pandas as pd
df = pd.DataFrame()
df['項目'] = keys
df['値'] = values

df.to_csv('情報.csv', index=False)
