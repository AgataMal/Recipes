#!/usr/bin/env python3

import unittest
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium import webdriver

class TestTitle(unittest.TestCase):

    def setUp(self):
        #firefox_profile="default-release"
        # executable_path=r'/usr/bin/geckodriver', firefox_profile="selenium"
        options = Options()
        options.add_argument("-profile")
        # put the root directory your default profile path here, you can check it by opening Firefox and then pasting 'about:profiles' into the url field 
        options.add_argument("/home/agatamalczyk/snap/firefox/common/.mozilla/firefox/mp3ljunm. selenium")
        self.driver = webdriver.Firefox(options=options)

    def test_search_in_python_org(self):
            driver = self.driver
            driver.get("http://192.168.1.150:5000/")
            self.assertIn("Recipes", driver.title)

            link_to_click = driver.find_element(By.XPATH, "//a[@href='/dumplings']")
            link_to_click.click()
            self.assertIn("dumplings", driver.title)

            link_to_click = driver.find_element(By.XPATH, "//a[@href='/']")
            link_to_click.click()
            self.assertIn("Recipes", driver.title)

            link_to_click = driver.find_element(By.XPATH, "//a[@href='/goulash']")
            link_to_click.click()
            self.assertIn("goulash", driver.title)

            link_to_click = driver.find_element(By.XPATH, "//a[@href='/']")
            link_to_click.click()
            self.assertIn("Recipes", driver.title)

            link_to_click = driver.find_element(By.XPATH, "//a[@href='/devolay']")
            link_to_click.click()
            self.assertIn("devolay", driver.title)

            link_to_click = driver.find_element(By.XPATH, "//a[@href='/']")
            link_to_click.click()
            self.assertIn("Recipes", driver.title)

            link_to_click = driver.find_element(By.XPATH, "//a[@href='/cheesecake']")
            link_to_click.click()
            self.assertIn("cheesecake", driver.title)

            link_to_click = driver.find_element(By.XPATH, "//a[@href='/']")
            link_to_click.click()
            self.assertIn("Recipes", driver.title)

            
    
    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()