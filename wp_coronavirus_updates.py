import requests
import bs4
from bs4 import BeautifulSoup
import json



def wp_corona_stats():
    r = requests.get('https://www.washingtonpost.com/world/2020/03/27/coronavirus-latest-news/')
    soup1 = bs4.BeautifulSoup(r.text,"lxml")

    titles = soup1.find_all('h2', {'class': 'gray-darkest font-lg font--headline mb-sm'})
    author = soup1.find_all('span', {'class': 'font-bold' })
    timeStamp = soup1.find_all('div', {'class': 'display-date'})
    content = soup1.find_all('div', {'data-qa': 'article-body'})
    return titles , content, timeStamp, author


titles, content, timeStamp, author = wp_corona_stats()


print(len(titles))
json_object = []
for i in range(0,len(titles)):

    date = "March 27, 2020 at "
    time = timeStamp[int(i+1)].text.replace(date,'')

    json_object.append(
       {
       "id": str(i),
       "time": str(time),
       "title": str(titles[int(i)].text),
       "author": str(author[int(i+10)].text),
       "content": str(content[int(i)].text)
       }
   )
j = json.dumps(json_object)
with open('wp_articles_03272020.json','w') as f:
    f.write(j)
    f.close()
