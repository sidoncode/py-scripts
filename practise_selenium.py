import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.webdriver import *
import unittest
import HtmlTestRunner
print(###########################
                                 ####################TERMINAL###########################
                                                                                ########################################
)
name = str(input("Enter the Username/e-Mail id for the completion of the order"))
passcode = str(input("Enter the passcode for the completion of the order"))


driver = webdriver.Chrome(executable_path="C:\Drivers\chromedriver_win32/chromedriver.exe")
#driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://www.amazon.in/")
driver.find_element_by_id("twotabsearchtextbox").send_keys("Apple iphone 11")
driver.find_element_by_xpath('/html/body/div[1]/header/div/div[1]/div[3]/div/form/div[2]/div/input').click()

driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/div[2]/div/span[3]/div[1]/div[1]/div/span/div/div/div/div/div[2]/div[2]/div/div[1]/div/div/div[1]/h2/a/span').click()
driver.find_element_by_xpath('//*[@id="buy-now-button"]').click()



time.sleep(10)

#driver.close()
#driver.quit()