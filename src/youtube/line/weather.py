import requests
from bs4 import BeautifulSoup

def today_weather():    #今日の天気スクレイピング
    url = 'https://tenki.jp/forecast/5/26/5110/23100/'
    res = requests.get(url)
    soup = BeautifulSoup(res.text, 'html.parser')

    #対象の要素
    weather = soup.find_all("p", class_="weather-telop")
    temp = soup.find_all("dd", class_="high-temp temp")
    low_temp = soup.find_all("dd", class_="low-temp temp")
    tds = soup.select("tr.rain-probability td")
    hini = soup.find_all("h3", class_="left-style")

    tenki = hini[0].getText() + "\n\n" + weather[0].getText()
    kion = "\n最高 " + temp[0].getText()
    low_kion = "  最低 " + low_temp[0].getText()
    rain1 = "\n\n降水確率\n00-06時  " + tds[0].getText()
    rain2 = "\n06-12時  " + tds[1].getText()
    rain3 = "\n12-18時  " + tds[2].getText()
    rain4 = "\n18-24時  " + tds[3].getText()


    a = tenki+kion+low_kion+rain1+rain2+rain3+rain4
    return a

def tomorow_wether():    #明日の天気スクレイピング
    url = 'https://tenki.jp/forecast/5/26/5110/23100/'
    res = requests.get(url)
    soup = BeautifulSoup(res.text, 'html.parser')

    #対象の要素
    weather = soup.find_all("p", class_="weather-telop")
    temp = soup.find_all("dd", class_="high-temp temp")
    low_temp = soup.find_all("dd", class_="low-temp temp")
    tds = soup.select("tr.rain-probability td")
    hini = soup.find_all("h3", class_="left-style")

    tenki = hini[1].getText() + "\n\n" + weather[1].getText()
    kion = "\n最高 " + temp[1].getText()
    low_kion = "  最低 " + low_temp[1].getText()
    rain1 = "\n\n降水確率\n00-06時  " + tds[4].getText()
    rain2 = "\n06-12時  " + tds[5].getText()
    rain3 = "\n12-18時  " + tds[6].getText()
    rain4 = "\n18-24時  " + tds[7].getText()

    b = tenki+kion+low_kion+rain1+rain2+rain3+rain4
    return b