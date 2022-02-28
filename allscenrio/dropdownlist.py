"""
select one option
capture options from drop down
count how many options present
"""

import time
from selenium import webdriver
from selenium.webdriver.support.ui import Select

CHROME_DRIVER_PATH = r'F:\Scoopons\selinium_work\chromedriver_win32\chromedriver.exe'

# create driver object
driver=webdriver.Chrome(executable_path=CHROME_DRIVER_PATH)

driver.get("https://fs2.formsite.com/meherpavan/form2/index.html?1537702596407")
drop_down_list_element=driver.find_element_by_id('RESULT_RadioButton-9')
drop_down_list=Select(drop_down_list_element)
driver.maximize_window()
#select by visible text
#drop_down_list.select_by_visible_text('Morning')

#select by index
drop_down_list.select_by_index(2) #it will select afternoon

#select by value
#drop_down_list.select_by_value("Radio-2")

#count number of options

print(len(drop_down_list.options))

#printing all opitons lists
all_options=drop_down_list.options

for option in all_options:
    print(option.text)

#capture all the options and print them as output
time.sleep(2)
driver.close()
