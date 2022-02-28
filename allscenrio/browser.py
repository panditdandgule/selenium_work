import time
from selenium import webdriver

CHROME_DRIVER_PATH= '/chromedriver_win32/chromedriver.exe'

#driver=webdriver.Chrome(executable_path=CHROME_DRIVER_PATH)

driver=webdriver.Edge(executable_path=r"/chromedriver_win32/MicrosoftEdgeSetup.exe")

APPLICATION_URL="https://newtours.demout.com"
driver.get(APPLICATION_URL)
time.sleep(2)
print(driver.title)

print(driver.current_url)

print(driver.page_source)

print(driver.close())