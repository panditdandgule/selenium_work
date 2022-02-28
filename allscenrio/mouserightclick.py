import time

from selenium import webdriver
from selenium.webdriver import ActionChains

CHROME_DRIVER_PATH = r'F:\Scoopons\selinium_work\chromedriver_win32\chromedriver.exe'

# create driver object
driver=webdriver.Chrome(executable_path=CHROME_DRIVER_PATH)

driver.get("https://swisnl.github.io/jQuery-contextMenu/demo.html")

buttonelement=driver.find_element_by_xpath("/html/body/div/section/div/div/div/p/span")

actions=ActionChains(driver)

actions.context_click(buttonelement).perform() #right click

time.sleep(4)

driver.close()