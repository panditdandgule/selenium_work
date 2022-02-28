import time

from selenium import webdriver
from selenium.webdriver import ActionChains


CHROME_DRIVER_PATH = r'F:\Scoopons\selinium_work\chromedriver_win32\chromedriver.exe'

# create driver object
driver=webdriver.Chrome(executable_path=CHROME_DRIVER_PATH)

driver.get("https://opensource-demo.orangehrmlive.com/")

print(driver.title)

driver.maximize_window()

username=driver.find_element_by_id("txtUsername").send_keys("Admin")
password=driver.find_element_by_id("txtPassword").send_keys("admin123")
btnlogin=driver.find_element_by_id("btnLogin").click()

admin=driver.find_element_by_id('menu_admin_viewAdminModule')
usermangement=driver.find_element_by_id('menu_admin_UserManagement')
users=driver.find_element_by_id('menu_admin_viewSystemUsers')

actions=ActionChains(driver)

actions.move_to_element(admin).move_to_element(usermangement).move_to_element(users).click().perform()

time.sleep(2)

driver.close()