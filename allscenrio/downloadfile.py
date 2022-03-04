from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

chromeOptions=Options()
chromeOptions.add_experimental_option("prefs",{"download_default_directory":
                                                  r"F:\Scoopons\selinium_work\selenium_codes\downloaded_files"})

CHROME_DRIVER_PATH = r'F:\Scoopons\selinium_work\chromedriver_win32\chromedriver.exe'
driver=webdriver.Chrome(executable_path=CHROME_DRIVER_PATH,chrome_options=chromeOptions)
driver.get("http://demo.automationtesting.in/FileDownload.html")

driver.maximize_window()

#How to download text file
driver.find_element_by_id('textbox').send_keys("testing file download")
driver.find_element_by_id('createTxt').click() #Generate file button
driver.find_element_by_id('link-to-download').click() #download link

time.sleep(2)

#How to download pdf file
driver.find_element_by_id('pdfbox').send_keys("pdf file download")
driver.find_element_by_id('createPdf').click()
driver.find_element_by_id('pdf-link-to-download').click()

time.sleep(2)

driver.close()