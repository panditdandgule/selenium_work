from selenium import webdriver
from selenium.webdriver.common import keys

#chrome setup driver path
CHROME_DRIVER_PATH = 'F:\\Scoopons\\selinium_work\\chromedriver_win32\\chromedriver.exe'

#create driver object
driver=webdriver.Chrome(executable_path=CHROME_DRIVER_PATH)

#Using driver object you can access all methods

APPLICATION_URL="http://newtours.demout.com/"
driver.get(APPLICATION_URL)

#print title of the page
title_of_webpage=driver.title
print(title_of_webpage)

#Returns current url of the page
print(driver.current_url)

#It will return html code
#print(driver.page_source)

#maximize window
driver.maximize_window()

#close current brower
driver.close()

#close all browsers
driver.quit()