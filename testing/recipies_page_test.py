#!/usr/bin/env python3

from time import sleep
import unittest
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium import webdriver

class TestTitle(unittest.TestCase):


    title_test_cases = {
        "//a[@href='/dumplings']": "dumplings",
        "//a[@href='/goulash']": "goulash",
        "//a[@href='/devolay']": "devolay",
        "//a[@href='/cheesecake']":"cheesecake"
    }


    def setUp(self):
        options = Options()
        options.add_argument("-profile")
        options.add_argument("/home/agatamalczyk/snap/firefox/common/.mozilla/firefox/mp3ljunm. selenium")
        self.driver = webdriver.Firefox(options=options)

    def test_pages(self):
        driver = self.driver
        driver.get("http://192.168.1.150:5000/")
        self.assertIn("Recipes", driver.title)

        for element_location  in self.title_test_cases:
            self.check_page(element_location, self.title_test_cases[element_location])


    def check_page(self, element_location, expected_value):
        link_to_click = self.driver.find_element(By.XPATH, element_location)
        link_to_click.click()
        self.assertIn(expected_value, self.driver.title)

        link_to_click = self.driver.find_element(By.XPATH, "//a[@href='/']")
        sleep(1)
        link_to_click.click()
        self.assertIn("Recipes", self.driver.title)

    
    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()