'''import requests 
from bs4 import BeautifulSoup 
  
URL = "http://www.indiamart.com/"
r = requests.get(URL) 
  
soup = BeautifulSoup(r.content,) 
print(soup.prettify()) '''


'''import requests
from bs4 import BeautifulSoup

result = requests.get("https://www.indiamart.com/")

print(result.status_code)
print(result.headers)
src = result.content


soup = BeautifulSoup(src, 'lxml')


links = soup.find_all("a")
print(links)
print("\n")


for link in links:
    if "About" in link.text:
        print(link)
        print(link.attrs['href'])'''


'''from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
import request as requests


products=[] 
prices=[] 
ratings=[]

#driver.get("https://www.indiamart.com/")
result = requests.get("https://www.indiamart.com/")

soup = BeautifulSoup(result)
for a in result.findAll('a',href=True, attrs={'class':'_31qSD5'}):
    name=a.find('div', attrs={'class':'_3wU53n'})
    price=a.find('div', attrs={'class':'_1vC4OE _2rQ-NK'})
    rating=a.find('div', attrs={'class':'hGSR34 _2beYZw'})
    products.append(name.text)
    prices.append(price.text)
    ratings.append(rating.text) 

df = pd.DataFrame({'Product Name':products,'Price':prices,'Rating':ratings}) 
df.to_csv('products.csv', index=False, encoding='utf-8')'''



import os 
import requests 
from bs4 import BeautifulSoup
import sys
import time

URL = "https://www.indiamart.com"
r = requests.get(URL) 
soup = BeautifulSoup(r.content,"lxml") 
#print(soup.prettify()) 
#print(soup.find_all(id = "cf_fb"))
#print(soup.find_all("a",c))
