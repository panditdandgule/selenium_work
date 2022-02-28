import time

from selenium import webdriver
from selenium.webdriver import ActionChains

CHROME_DRIVER_PATH = r'F:\Scoopons\selinium_work\chromedriver_win32\chromedriver.exe'

# create driver object
driver=webdriver.Chrome(executable_path=CHROME_DRIVER_PATH)

driver.get("https://testautomationpractice.blogspot.com")

driver.maximize_window()

print(driver.title)

element=driver.find_element_by_xpath("//*[@id='HTML10']/div[1]/button")

actions=ActionChains(driver)

actions.double_click(element).perform() #dubole click on button

time.sleep(2)
driver.close()