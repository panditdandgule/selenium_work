import time
from selenium import webdriver
from selenium.webdriver.common.by import By


CHROME_DRIVER_PATH = r'F:\Scoopons\selinium_work\chromedriver_win32\chromedriver.exe'

driver=webdriver.Chrome(executable_path=CHROME_DRIVER_PATH)

driver.get("http://demo.automationtesting.in/Windows.html")

driver.find_element_by_xpath("//*[@id='Tabbed']/a/button").click()

print(driver.current_window_handle) #this will pring current windows(parent window)

#Returns all the handle values of opened browser windows
handles=driver.window_handles

for handle in handles:
    driver.switch_to.window(handle)
    print(driver.title)
    if driver.title=="Frames & windows":
        driver.close()

driver.close()