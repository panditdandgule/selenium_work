from selenium import webdriver
from selenium.webdriver import common
from selenium.webdriver.common.alert import Alert

CHROMEDRIVERPATH=r'F:\Scoopons\selinium_work\chromedriver_win32\chromedriver.exe'

chromeDriver=webdriver.Chrome(executable_path=CHROMEDRIVERPATH)
chromeDriver.get('https://demoqa.com/alerts')

alert1=Alert(chromeDriver)
chromeDriver.find_element_by_id('alertButton').click()
alert1.accept()

alert2=Alert(chromeDriver)
chromeDriver.find_element_by_id('timerAlertButton').click()
alert2.accept()