# -*- coding: utf-8 -*-
"""
Created on Mon Dec 13 14:07:25 2021

@author: bbalushev
"""

from selenium import webdriver
from seleniumwire import webdriver as wire_webdriver
from seleniumwire.webdriver import ChromeOptions
from source.web_source.web import Web

chrome_options = ChromeOptions()
edge_options = {'port': 12345}


# ============================= Loading web browser function =============================
def get_web(browser: str) -> object:
    """ get_web function start web browser driver set on 'browser' input parameter
        or will raise the 'Unsupported browser' error

        Function attribute:
            browser -> contains the name of the browser

        Return value -> web object

    """

    browser_lower_case_name = browser.lower()

    if browser_lower_case_name == "chrome":
        return Web(wire_webdriver.Chrome(executable_path='drivers/chromedriver.exe'))
    elif browser_lower_case_name == "firefox":
        return Web(wire_webdriver.Firefox(executable_path='drivers/geckodriver.exe'))
    elif browser_lower_case_name == "edge":
        return Web(wire_webdriver.Edge(executable_path='drivers/msedgedriver.exe',
                                       seleniumwire_options=edge_options))
    elif browser_lower_case_name == "ie":
        return Web(webdriver.Ie(executable_path='drivers/IEDriverServer.exe'))
    elif browser_lower_case_name == "headless":
        chrome_options.add_argument('headless')
        chrome_options.add_argument("window-size=1080,1920")
        return Web(wire_webdriver.Chrome(executable_path='drivers/chromedriver.exe',
                                         chrome_options=chrome_options))
    else:
        raise Exception('Unsupported browser!')


# =========================== Set web browser in to mobile view function  ===========================
def change_browser_to_mobile(mobile_device_name: str) -> None:
    """ change_browser_to_mobile function set web browser options to the mobile view

        Function attribute:
            mobile_device_name -> contains the name of the browser

        Return value -> None

    """

    chrome_options.add_experimental_option('mobileEmulation', {'deviceName': mobile_device_name})


# ================================ Remove alerts function ================================
def remove_alerts() -> None:
    """ remove_alerts function removes all web browser notifications

        Function attribute -> None
        Return value -> None

    """

    prefs = {"profile.default_content_setting_values.notifications": 2}
    chrome_options.add_experimental_option("prefs", prefs)
