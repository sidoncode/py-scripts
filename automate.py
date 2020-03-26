import selenium.webdriver as webdriver
from selenium.webdriver import Firefox
import selenium.webdriver.support.ui as ui
from selenium.webdriver.common.keys import Keys

import time

path = "C:\\Users\\Sidd\\Downloads\\geckodriver\\geckodriver.exe"
driver = Firefox(executable_path=path)

def stirringminds():

    driver.get("https://stirringminds.com/")

    driver.maximize_window()

    time.sleep(19)
    driver.minimize_window()
    time.sleep(19)
    driver.maximize_window()
    time.sleep(19)
    driver.minimize_window()
    time.sleep(19)
    driver.maximize_window()

    time.sleep(10)

    driver.find_element_by_xpath('//*[@id="menu-pranav-top-2-only-home-1"]/li[7]/a').click()
    time.sleep(1)


def konsalidon():
    driver.get("https://konsalidon.com/")
    time.sleep(20)
    driver.minimize_window()
    time.sleep(19)
    driver.maximize_window()
    time.sleep(19)
    driver.minimize_window()
    time.sleep(19)
    driver.maximize_window()
    time.sleep(10)

def advisory_city():
    driver.get("https://advisory.city/")
    time.sleep(10)
    driver.maximize_window()
    time.sleep(12)
    driver.minimize_window()
    time.sleep(12)
    driver.maximize_window()
    time.sleep(19)
    driver.minimize_window()
    time.sleep(19)
    driver.maximize_window()
    time.sleep(19)
    driver.minimize_window()
    time.sleep(19)
    driver.maximize_window()
    time.sleep(10)
    driver.find_element_by_xpath('//*[@id="primary-menu"]/li[1]/a/span/span').click() #freezone
    time.sleep(12)
    time.sleep(19)
    driver.minimize_window()
    time.sleep(19)
    driver.maximize_window()
    time.sleep(19)
    driver.minimize_window()
    time.sleep(19)
    driver.maximize_window()
    time.sleep(10)
    driver.find_element_by_xpath('//*[@id="primary-menu"]/li[2]/a/span/span').click() #ecosystem
    time.sleep(12)
    time.sleep(19)
    driver.minimize_window()
    time.sleep(19)
    driver.maximize_window()
    time.sleep(19)
    driver.minimize_window()
    time.sleep(19)
    driver.maximize_window()
    time.sleep(10)

    driver.find_element_by_xpath('//*[@id="primary-menu"]/li[3]/a/span/span').click() #support service
    time.sleep(12)
    time.sleep(19)
    driver.minimize_window()
    time.sleep(19)
    driver.maximize_window()
    time.sleep(19)
    driver.minimize_window()
    time.sleep(19)
    driver.maximize_window()
    time.sleep(10)

    driver.find_element_by_xpath('//*[@id="primary-menu"]/li[4]/a/span/span').click() #lead generation
    time.sleep(12)
    time.sleep(19)
    driver.minimize_window()
    time.sleep(19)
    driver.maximize_window()
    time.sleep(19)
    driver.minimize_window()
    time.sleep(19)
    driver.maximize_window()
    time.sleep(10)
    driver.find_element_by_xpath('//*[@id="primary-menu"]/li[5]/a/span/span').click() #research support
    time.sleep(19)
    driver.minimize_window()
    time.sleep(19)
    driver.maximize_window()
    time.sleep(19)
    driver.minimize_window()
    time.sleep(19)
    driver.maximize_window()
    time.sleep(10)
    time.sleep(12)
    driver.find_element_by_xpath('//*[@id="primary-menu"]/li[6]/a/span/span').click() #conatct
    time.sleep(19)
    driver.minimize_window()
    time.sleep(19)
    driver.maximize_window()
    time.sleep(19)
    driver.minimize_window()
    time.sleep(19)
    driver.maximize_window()
    time.sleep(10)


 

for i in range(0,99):
    konsalidon();
    
    #driver.close()

    stirringminds();

    time.sleep(22)

    advisory_city();

    time.sleep(1)




'''
last_height = driver.execute_script("return document.body.scrollHeight")


for i in range(0,100):
    # Scroll down to bottom
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    # Wait to load page
    time.sleep(SCROLL_PAUSE_TIME)

    # Calculate new scroll height and compare with last scroll height
    new_height = driver.execute_script("return document.body.scrollHeight")
    last_height = driver.execute_script("return document.body.scrollHeight")



first_result = ui.WebDriverWait(driver, 15).until(lambda driver: driver.find_element_by_class_name('rc'))
first_link = first_result.find_element_by_tag_name('a')

main_window = driver.current_window_handle
first_link.send_keys(Keys.CONTROL + Keys.RETURN)
driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + Keys.TAB)
driver.switch_to_window(main_window)
sleep(2)
driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + 'w')
driver.switch_to_window(main_window)
'''