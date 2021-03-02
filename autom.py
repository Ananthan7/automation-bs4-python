import requests
from bs4 import BeautifulSoup

res = requests.get('https://www.lipsum.com/')
soup = BeautifulSoup(res.text, 'html.parser')

posts = soup.find(id='Panes').get_text()

print(posts)