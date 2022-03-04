import time

from selenium import webdriver

CHROME_DRIVER_PATH = r'F:\Scoopons\selinium_work\chromedriver_win32\chromedriver.exe'
filepath=r'F:\Scoopons\selinium_work\selenium_codes\allscenrio\Mainpage.png'

driver=webdriver.Chrome(executable_path=CHROME_DRIVER_PATH)

driver.get('https://testautomationpractice.blogspot.com/')

print(driver.current_window_handle)
print(driver.current_url)
print(driver.title)

driver.switch_to.frame(0)

driver.find_element_by_id('RESULT_FileUpload-10').send_keys(filepath)

time.sleep(2)