from selenium import webdriver
import time

CHROME_DRIVER_PATH = r'F:\Scoopons\selinium_work\chromedriver_win32\chromedriver.exe'
url='https://opensource-demo.orangehrmlive.com/'

driver=webdriver.Chrome(executable_path=CHROME_DRIVER_PATH)

driver.get("https://testautomationpractice.blogspot.com")

driver.maximize_window()

driver.find_element_by_xpath("//*[@id='HTML9']/div[1]/button").click()

time.sleep(5)

#driver.switch_to_alert().accept() #closes alert window with okay button

driver.switch_to_alert().dismiss() #closes alert window with cancel button

time.sleep(2)

driver.close()