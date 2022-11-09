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
        user = "instructo"       #must be a valid username for theapplication
        pwd = "maverick1"         #must be the password for a valid user
        #open the browser and go to the admin page
        driver = self.driver
        driver.maximize_window()
        driver.get("http://127.0.0.1:8000/admin")
        #find the username and password input boxes on the screen by ID
        #send the username and password to each box
        #send the Return (Enter) key to the system
        #go to the main application page
        elem = driver.find_element(By.ID, "id_username")
        elem.send_keys(user)
        elem = driver.find_element(By.ID, "id_password")
        elem.send_keys(pwd)
        time.sleep(10)
        elem.send_keys(Keys.RETURN)
        time.sleep(10)
        driver.get("http://127.0.0.1:8000")
        time.sleep(10)
        try:
           elem = driver.find_element(By.LINK_TEXT, "Login")
           print("Test Passed - Invalid username")
           assert True
        #else report that the test failed
        except NoSuchElementException:
            self.fail("Login Failed - user may not exist")
    def tearDown(self):
        self.driver.close()
if __name__ == "__main__":
    unittest.main()