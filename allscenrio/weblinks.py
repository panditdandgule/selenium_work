import sys
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

CHROME_DRIVER_PATH = r'F:\Scoopons\selinium_work\chromedriver_win32\chromedriver.exe'

driver=webdriver.Chrome(executable_path=CHROME_DRIVER_PATH)

driver.get('https://opensource-demo.orangehrmlive.com/')


links=driver.find_elements(By.TAG_NAME,"a")


for link in links:
    print(link.text)

#clicking on the link

#driver.find_element(By.LINK_TEXT,"Forgot your password?").click() #we need to specify full STRING EX. REGISTER

driver.find_element(By.PARTIAL_LINK_TEXT,"Forgot").click()#specify sub string EX. REG

time.sleep(2)

driver.close()