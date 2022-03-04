from selenium import webdriver

CHROME_DRIVER_PATH = r'F:\Scoopons\selinium_work\chromedriver_win32\chromedriver.exe'
driver=webdriver.Chrome(executable_path=CHROME_DRIVER_PATH)
driver.get("https://www.countries-ofthe-world.com/flags-of-the-world.html")

driver.maximize_window()

#Scroll down page by pixel (min to max(0-1000))
#driver.execute_script("window.scrollBy(0,1000)","")

#scroll down page till the element is visible
#flag=driver.find_element_by_xpath("//*[@id='content']/div[2]/div[2]/table[1]/tbody/tr[86]/td[1]/img")
#driver.execute_script("arguments[0].scrollIntoView();",flag)

#scroll down page till end
driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")



driver.close()