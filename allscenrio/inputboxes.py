"""
How to find how many inputboxes present in web page
How to provide value into text box
How to get status of input boxes
"""

import time

from selenium import webdriver
from selenium.webdriver.common.by import By

CHROME_DRIVER_PATH = r'F:\Scoopons\selinium_work\chromedriver_win32\chromedriver.exe'
# create driver object

driver = webdriver.Chrome(executable_path=CHROME_DRIVER_PATH)

driver.get("https://fs2.formsite.com/meherpavan/form2/index.html?1537702596407")

driver.maximize_window()

print(driver.title)

# How to find how many inputboxes present in web page
inputboxes = driver.find_elements(By.CLASS_NAME, 'text_field')

total_inputboxes = len(inputboxes)

print(total_inputboxes)

# How to get the status of the input boxes
status = first_name = driver.find_element(By.ID, 'RESULT_TextField-1').is_displayed()
print("Checking Displayed Or Not: ", status)  # It will print True/False

status1 = first_name = driver.find_element(By.ID, 'RESULT_TextField-1').is_enabled()
print("Checking Enabled Or Not: ", status1)  # It will print True/False

# How to provide value into text box
# first way
first_name = driver.find_element(By.ID, 'RESULT_TextField-1').send_keys("pavan")
last_name = driver.find_element(By.ID, "RESULT_TextField-2").send_keys("patil")

# second way
phone_number = driver.find_element_by_id("RESULT_TextField-3").send_keys("9756455523")

time.sleep(2)
driver.close()
