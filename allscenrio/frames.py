import sys

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

CHROME_DRIVER_PATH = r'F:\Scoopons\selinium_work\chromedriver_win32\chromedriver.exe'


driver=webdriver.Chrome(executable_path=CHROME_DRIVER_PATH)

driver.get("https://seleniumhq.github.io/selenium/docs/api/java/index.html")

driver.switch_to.frame("packageListFrame")
driver.find_element_by_link_text('org.openqa.selenium').click() #first frame

time.sleep(3)
driver.switch_to.default_content() #go back main page"

driver.switch_to.frame("packageFrame") #second frame
driver.find_element_by_link_text("WebDriver").click() #second frame

time.sleep(3)
driver.switch_to.default_content()

driver.switch_to.frame("classFrame").click()

time.sleep(3)

driver.close()
