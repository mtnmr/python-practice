import requests
from bs4 import BeautifulSoup

url = ''
res = requests.get(url)

soup = BeautifulSoup(res.text, 'html.parser')
print(soup.prettify)

soup.find_all('p')
soup.find('p')
soup.p  #上記と同じ意味

subscribers = soup.find_all('p', attrs={'class':'subscribers'})[0]

n_subscribers = int(subscribers.text.split(':')[1])




