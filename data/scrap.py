# import selenium
from bs4 import BeautifulSoup
import requests

url = "https://farsi.palinfo.com/categories/%DA%AF%D8%B2%D8%A7%D8%B1%D8%B4"
res = requests.get(url,timeout=(2000,2000)).content
doc = BeautifulSoup(res,"html.parser")
# /////////////////////////////////////////////
# from requests_html import HTMLSession
# s = HTMLSession()
# response = s.get(url)
# response.html.render()
# print(response)

# /////////////////////////////////////////////
doc = doc.body.form.div.next_sibling.div.div.div.next_sibling
doc = doc.div.next_sibling.div.div.div.next_sibling.next_sibling
doc = doc.div.next_sibling.div
print(doc)
print(doc.ul)
div = doc.find(class_='studieslist listNews listNewsBelowLeft Marginswiper')
print(div)
