


class BasePage():
    def __init__(self, driver):
        self.driver = driver

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

    def assert_word(self, word, result):
        value_word = word.text
        assert value_word == result
        print("Assert word - PASSED")