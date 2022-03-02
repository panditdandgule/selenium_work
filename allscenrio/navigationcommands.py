import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

CHROME_DRIVER_PATH = r'F:\Scoopons\selinium_work\chromedriver_win32\chromedriver.exe'

# create driver object
driver=webdriver.Chrome(executable_path=CHROME_DRIVER_PATH)

driver.get("http://newtours.demoaut.com/")#FR application

print(driver.title)

driver.get("http://pavantestingtools.blogspot.in/") #testing tool

time.sleep(5)

print(driver.title)

driver.back()

time.sleep(5)
print(driver.title)

driver.forward()

print(driver.title)

time.sleep(5)