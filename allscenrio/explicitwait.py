import time

from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

CHROME_DRIVER_PATH = r'F:\Scoopons\selinium_work\chromedriver_win32\chromedriver.exe'
url='https://opensource-demo.orangehrmlive.com/'

driver =webdriver.Chrome(executable_path=CHROME_DRIVER_PATH)

driver.implicitly_wait(5)

driver.maximize_window()

driver.get('http://www.expedia.com/')

driver.find_element_by_id("tab-flight-tab-hp").click() #flight button


driver.find_element_by_id("flight-origin-hp-flight").send_keys('xxx')#source
time.sleep(2) #from python
driver.find_element_by_id("flight-destination-hp-flight").send_keys('NYX') #destination

driver.find_element_by_id("flight-departing-hp-flight").clear()
driver.find_element_by_id("flight-departing-hp-flight").send_keys("12/10/2022")
driver.find_element_by_id("flight-returning-hp-flight").clear()
driver.find_element_by_id("flight-returning-hp-flight").send_keys("12/15/2022")

driver.find_element_by_id("gcw-flights-form-hp-flight").click()

wait=WebDriverWait(driver,10)
element=wait.until(EC.element_to_be_clickable(driver.find_element('stopFilter_stops-0')))
element.click()

time.sleep(3)

driver.quit()

