import time

from selenium import webdriver


CHROME_DRIVER_PATH = r'F:\Scoopons\selinium_work\chromedriver_win32\chromedriver.exe'
# create driver object
driver=webdriver.Chrome(executable_path=CHROME_DRIVER_PATH)

APPLICATION_URL="https://fs2.formsite.com/meherpavan/form2/index.html?1537702596407"
driver.get(APPLICATION_URL)

#How to work with radio buttons
status=driver.find_element_by_id("RESULT_RadioButton-7_0").is_selected() #True/False
print(status) #If selected radio button its return True otherwise False

driver.maximize_window()

#click is method is automatically select radio buttons
driver.find_element_by_id("RESULT_RadioButton-7_0").click() #select radio buttion

status=driver.find_element_by_id("RESULT_RadioButton-7_0").is_selected() #True/False
print(status) #If selected radio button its return True otherwise False

#working with check boxes
driver.find_element_by_id("RESULT_CheckBox-8_0").click() #sunday
driver.find_element_by_id("RESULT_CheckBox-8_6").click() #satuarday

time.sleep(2)
driver.close()