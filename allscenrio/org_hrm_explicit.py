from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains

CHROMEDRIVERPATH=r'F:\Scoopons\selinium_work\chromedriver_win32\chromedriver.exe'

def launch_browser():
    chromeDriver=webdriver.Chrome(executable_path=CHROMEDRIVERPATH)
    chromeDriver.get('https://opensource-demo.orangehrmlive.com/')
    chromeDriver.maximize_window()
    print("Url:",chromeDriver.current_url)
    print("Webpage Title: ",chromeDriver.title)
    chromeDriver.implicitly_wait(10)
    return chromeDriver



chromeDriver=launch_browser()
wait=WebDriverWait(chromeDriver,10)
try:
    wait.until(EC.element_to_be_clickable(By.ID,'txtUsername1'))
except:
    print("something went wrong")


chromeDriver.find_element_by_id('txtUsername').send_keys('Admin')
chromeDriver.find_element_by_id('txtPassword').send_keys('admin123')
chromeDriver.find_element_by_id('btnLogin').click()

