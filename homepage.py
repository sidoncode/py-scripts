from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
import time

browser = webdriver.Chrome()
browser.get("http://www.indiamart.com") # Load page

time.sleep(0.2)

#top nav elements
elems = browser.find_elements_by_xpath("/html/body/div[4]/div[2]/div[1]/div[12]/div[6]/h2/a[1]")

for e in elems:
    print(e.get_attribute('text'))

browser.close()
