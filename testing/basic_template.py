#!/usr/bin/env python3

import unittest
from selenium.webdriver.firefox.options import Options
from selenium import webdriver

class TestTitle(unittest.TestCase):

    def setUp(self):
        options = Options()
        # Firefox installed from snap workaround
        options.add_argument("-profile")
        options.add_argument("/home/agatamalczyk/snap/firefox/common/.mozilla/firefox/mp3ljunm. selenium")
        # -----------------------------------------
        self.driver = webdriver.Firefox(options=options)

    def test_search_in_python_org(self):
            driver = self.driver
            driver.get("http://192.168.1.150:5000")
            self.assertEqual("Recipes", driver.title)
    
    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()