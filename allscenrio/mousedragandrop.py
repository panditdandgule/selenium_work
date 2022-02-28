import time

from selenium import webdriver
from selenium.webdriver import ActionChains


CHROME_DRIVER_PATH = r'F:\Scoopons\selinium_work\chromedriver_win32\chromedriver.exe'

# create driver object
driver=webdriver.Chrome(executable_path=CHROME_DRIVER_PATH)

driver.get("http://www.dhtmlgoodies.com/scripts/drag-drop-custom/demo-drag-drop-3.html")

print(driver.title)

driver.maximize_window()

source_element=driver.find_element_by_id('box6')
target_element=driver.find_element_by_id('box106')

actions=ActionChains(driver)

actions.drag_and_drop(source_element,target_element).perform()

time.sleep(4)

driver.close()