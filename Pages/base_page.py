import time
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver


class BasePage():
    def __init__(self, driver):
        self.driver = driver
        self.SELECTED_PRODUCT=[]
        self.CART_PRODUCT=[]

    """Method get current url"""

    def get_current_url(self):
        get_url = self.driver.current_url
        print("Current url: " + get_url)


    def get_element(self, by, locator):
        return self.driver.find_element(by, locator)

    """Method Screenshot"""



    """Method assert url"""

    def assert_url(self, result):
        get_url = self.driver.current_url
        assert get_url == result
        print("Assert url - PASSED")

    """Method assert page text"""

