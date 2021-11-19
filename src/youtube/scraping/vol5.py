import requests
from bs4 import BeautifulSoup

url = 'https://scraping-for-beginner.herokuapp.com/image'
res = requests.get(url)

soup = BeautifulSoup(res.text, 'html.parser')

#画像を１つ取得
img_tag = soup.find('img')

root_url = 'https://scraping-for-beginner.herokuapp.com' 
img_url = root_url + img_tag['src']

from PIL import Image   #画像の保存に使う
import io               #ファイルの入出力を行う

img = Image.open(io.BytesIO(requests.get(img_url).content))
img.save('img/sample.jpg') #imgというフォルダにsample.jpgとして保存



#上記をまとめて全部の画像を取得する

soup = BeautifulSoup(res.text, 'html.parser')

img_tags = soup.find_all('img')
for i, img_tag in enumerate(img_tags):
    root_url = 'https://scraping-for-beginner.herokuapp.com' 
    img_url = root_url + img_tag['src']

    img = Image.open(io.BytesIO(requests.get(img_url).content))
    img.save(f'img/{i}.jpg')
