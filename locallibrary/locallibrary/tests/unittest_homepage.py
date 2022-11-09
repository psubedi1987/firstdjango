import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import warnings

class ll_ATS(unittest.TestCase):
    #set up the test class - assign the driver to Chrome - if using adifferent
    #browser, change the browser name below
    def setUp(self):
        self.driver = webdriver.Safari()
        warnings.simplefilter('ignore', ResourceWarning) #ignore resources warning if occurs
    # If login is successful, 'Logout' will be displayed as the text in the navbar
    def test_ll(self):
        user = ""       #must be a valid username for theapplication
        pwd = ""         #must be the password for a valid user
        #open the browser and go to the admin page
        driver = self.driver
        driver.maximize_window()
        driver.get("http://127.0.0.1:8000")
        time.sleep(8) # pause to allow screen to load
        elem = driver.find_element(By.XPATH,'/html/body/div/div/div[1]/ul/li[1]/a').click()
        time.sleep(8)
        try:
            elem = driver.find_element(By.XPATH,'/html/body/div/div/div[1]/ul/li[1]/a')

            print ("Test passed-Home page Displayed")
            assert True
        except NoSuchElementException:
            self.fail("Home page does not appear - test failed")

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()