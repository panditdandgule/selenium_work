import time
from selenium import webdriver

CHROME_DRIVER_PATH = r'F:\Scoopons\selinium_work\chromedriver_win32\chromedriver.exe'
url='https://opensource-demo.orangehrmlive.com/'

driver =webdriver.Chrome(executable_path=CHROME_DRIVER_PATH)

driver.get(url) #Opening URL TAKES SOME TIME

driver.implicitly_wait(10) #seconds

print(driver.title)

assert "OrangeHRM" in driver.title

username=driver.find_element_by_id('txtUsername').send_keys('Admin')
password=driver.find_element_by_id('txtPassword').send_keys('admin123')
driver.find_element_by_id('btnLogin').click()