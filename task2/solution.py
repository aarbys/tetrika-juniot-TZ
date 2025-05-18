from bs4 import BeautifulSoup
import requests
import pandas as pd
urlwiki = 'https://ru.wikipedia.org'
url = 'https://ru.wikipedia.org/wiki/Категория:Животные_по_алфавиту'

dct = dict()
while True:
    # empty dict => false
    if bool(dct):
        url_parse = urlwiki+l
    else:
        url_parse = url
        
    page = requests.get(url_parse)
    soup = BeautifulSoup(page.text, "html.parser")
    a = soup.find(class_="mw-category mw-category-columns").find_all('a')

    for i in a:
        name = i.text
       
        try:
            dct[name[0].upper()] +=1
        except KeyError:
            dct[name[0].upper()] = 1
    try:
        l = soup.find(lambda tag:tag.name=="a" and "Следующая страница" in tag.text)['href']
    except TypeError:
        break

df = pd.DataFrame.from_dict(dct, orient="index")
df.to_csv("data.csv",encoding="utf-8",header=False)
