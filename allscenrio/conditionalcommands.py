import time

from selenium import webdriver
from selenium.webdriver.support import *
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains

CHROME_DRIVER_PATH = r'F:\Scoopons\selinium_work\chromedriver_win32\chromedriver.exe'

# create driver object
driver=webdriver.Chrome(executable_path=CHROME_DRIVER_PATH)

driver.get("https://opensource-demo.orangehrmlive.com/")

print(driver.title)

username=driver.find_element_by_id('txtUsername')
#Returs true or false based of element status
print(username.is_displayed())
print(username.is_enabled())

password=driver.find_element_by_id('txtPassword')
#Returs true or false based of element status
print(password.is_displayed())
print(password.is_enabled())

username.send_keys('Admin')
password.send_keys('admin123')

driver.find_element_by_id('btnLogin').click()

admin=driver.find_element_by_id('menu_admin_viewAdminModule')
usrmng=driver.find_element_by_id('menu_admin_UserManagement')
user=driver.find_element_by_id('menu_admin_viewSystemUsers')

actions=ActionChains(driver)
actions.move_to_element(admin).move_to_element(usrmng).move_to_element(user).click().perform()

checkbox=driver.find_element_by_id('ohrmList_chkSelectAll')

print("Status of checkbox:",checkbox.is_enabled())
print("Status of select or not checkbox",checkbox.is_selected())

time.sleep(2)
#driver.close()