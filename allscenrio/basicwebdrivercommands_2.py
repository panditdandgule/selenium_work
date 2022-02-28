from selenium import webdriver

#chrome setup driver path
CHROME_DRIVER_PATH = 'F:\\Scoopons\\selinium_work\\chromedriver_win32\\chromedriver.exe'

#create driver object
driver=webdriver.Chrome(executable_path=CHROME_DRIVER_PATH)

#get url
driver.get("https://www.googl.com")

driver.maximize_window()

print(driver.title)

print(driver.current_url)

driver.close()