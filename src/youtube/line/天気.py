import requests
from bs4 import BeautifulSoup

def today_weather():    #今日の天気スクレイピング
    url = 'https://tenki.jp/forecast/5/26/5110/23100/'
    res = requests.get(url)
    soup = BeautifulSoup(res.text, 'html.parser')

    #対象の要素
    weather = soup.find_all("p", attrs = {'class':'weather-telop'})
    temp = soup.find_all("dd", attrs = {'class':'high-temp temp'})
    low_temp = soup.find_all("dd", attrs = {'class':'low-temp temp'})
    tds = soup.select("tr.rain-probability td")
    hini = soup.find_all("h3", attrs = {'class':'left-style'})

    tenki = hini[0].text + "\n\n" + weather[0].text
    kion = "\n最高 " + temp[0].text
    low_kion = "  最低 " + low_temp[0].text
    rain1 = "\n\n降水確率\n00-06時  " + tds[0].text
    rain2 = "\n06-12時  " + tds[1].text
    rain3 = "\n12-18時  " + tds[2].text
    rain4 = "\n18-24時  " + tds[3].text

    a = tenki+kion+low_kion+rain1+rain2+rain3+rain4
    return a

def tomorow_wether():    #明日の天気スクレイピング
    url = 'https://tenki.jp/forecast/5/26/5110/23100/'
    res = requests.get(url)
    soup = BeautifulSoup(res.text, 'html.parser')

    #対象の要素
    weather = soup.find_all("p", attrs = {'class':'weather-telop'})
    temp = soup.find_all("dd", attrs = {'class':'high-temp temp'})
    low_temp = soup.find_all("dd", attrs = {'class':'low-temp temp'})
    tds = soup.select("tr.rain-probability td")
    hini = soup.find_all("h3", attrs = {'class':'left-style'})

    tenki = hini[1].text + "\n\n" + weather[1].text
    kion = "\n最高 " + temp[1].text
    low_kion = "  最低 " + low_temp[1].text
    rain1 = "\n\n降水確率\n00-06時  " + tds[4].text
    rain2 = "\n06-12時  " + tds[5].text
    rain3 = "\n12-18時  " + tds[6].text
    rain4 = "\n18-24時  " + tds[7].text

    b = tenki+kion+low_kion+rain1+rain2+rain3+rain4
    return b