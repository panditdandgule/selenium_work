import unittest

from selenium import webdriver

class Test(unittest.TestCase):

    def testName(self):
        CHROME_DRIVER_PATH = 'F:\\Scoopons\\selinium_work\\chromedriver_win32\\chromedriver.exe'

        driver=webdriver.Chrome(executable_path=CHROME_DRIVER_PATH)

        #IsNone means is None value it return True but we have driver value
        #self.assertIsNone(driver) #this driver varibale contains some value or not
        driver1=None
        self.assertIsNone(driver1)

        self.assertIsNotNone(driver) #the driver value should not None; it contains some value


if __name__=='__main__':
    unittest.main()