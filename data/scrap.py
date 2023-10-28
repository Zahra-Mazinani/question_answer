# import selenium
from bs4 import BeautifulSoup
import requests

url = "https://www.tasnimnews.com/fa/search?query=%D9%81%D9%84%D8%B3%D8%B7%DB%8C%D9%86&date=1"
res = requests.get(url).text
doc = BeautifulSoup(res,"html.parser",features="lxml")
print(doc)

# print(soup.prettify())
