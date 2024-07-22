import requests
from bs4 import BeautifulSoup


def getnew():
    title = []
    r = requests.get('https://baomoi.com/tag/LITE.epi')
    soup = BeautifulSoup(r.text, 'html.parser')

    mydiv = soup.find_all('h3', class_='font-semibold block')
    for new in mydiv:
        link = 'https://baomoi.com' + new.find('a')['href']
        title.append(link)
    print(title)
    return title
