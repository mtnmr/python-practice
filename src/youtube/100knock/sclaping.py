#install webdriver_manager

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

browser = webdriver.Chrome(ChromeDriverManager().install())

url = ''
browser.get(url)

elem_username = browser.find_element_by_id('HTML_username')
elem_username.send_keys('')

elem_password = browser.find_element_by_id('HTML_password')
elem_password.send_keys('')


login_btn = browser.find_element_by_id('HTML_loginbtn')
login_btn.click()

