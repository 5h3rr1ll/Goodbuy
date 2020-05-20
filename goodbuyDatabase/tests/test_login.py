import os
import unittest

from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class TestLogIn(unittest.TestCase):
    def setUp(self):
        options = Options()
        options.add_argument("--headless")
        self.driver = webdriver.Chrome(
            executable_path=str(os.environ.get("CHROMEDRIVER_PATH")),
            chrome_options=options,
        )

    def test_signup_chrome(self):
        self.driver.get("http://localhost:8000/login/")
        self.driver.find_element_by_id("id_username").send_keys("test_user")
        self.driver.find_element_by_id("id_password").send_keys("Test123456")
        self.driver.find_element_by_id("login-button").click()
        self.assertEqual(
            "http://localhost:8000/", self.driver.current_url
        )

    def tearDown(self):
        self.driver.quit
