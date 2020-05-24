#!/usr/bin/python3
# *_* coding: utf-8 *_*

"""
This module handles all options needed to be set for Chrome in Selenium
"""

import os

from selenium.webdriver.chrome.options import Options


def options():
    options = Options()
    options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
    options.add_argument("--headless")
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    options.add_argument("user-agent=Anon")
    prefs = {"profile.managed_default_content_settings.images": 2}
    options.add_experimental_option("prefs", prefs)
    return options
