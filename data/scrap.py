# import selenium
from bs4 import BeautifulSoup
import requests
import dataset

con = dataset.sql_connection()
# dataset.sql_table(con)


for i in range(700927,900000):
    
    url = 'https://www.asriran.com/fa/news/{}'.format(i)
    print(url)
    res = requests.get(url).content
    doc = BeautifulSoup(res,"html.parser")
    
    title = doc.find_all("div", {"class": "title"})
    for tag in title:
        for element in tag.find_all("a"):
            aTitle = element.text
            # print(aTitle)
    
    content = doc.find_all("div", {"class": "body"})
    for tag in content:
        for element in tag.find_all("p"):
            pContent = element.text
            # print(pContent)
    id = i-700000
    dataset.insertMultipleRecords(con,[(id,aTitle,pContent)])
    # break   
