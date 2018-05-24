from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome('C:\chromedriver_win32\chromedriver.exe')      

username = "akhildabral02@gmail.com"
password = "Classicdamon2#"

## Intializing Chrome Driver



## Opening Facebook Page

driver.get("http://facebook.com")

## Finding elements

element = driver.find_element_by_id("email")
element.send_keys(username)

## Find Password element

element = driver.find_element_by_id("pass")
element.send_keys(password)


## Press Login Button

element.send_keys(Keys.RETURN)

## Close Driver
driver.close()


