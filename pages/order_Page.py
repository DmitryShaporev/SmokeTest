from faker import Faker
from pages.base_page import *

fake=Faker()
class Order_Page(BasePage):

    def __init__(self,driver):
        super().__init__(driver)
        self.driver=driver


        # locators
    name="//input[@id='checkout_1']"
    email="//input[@id='checkout_2']"
    phone="//input[@id='checkout_3']"

        #getters
    def get_name(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.name)))

    def get_email(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.email)))

    def get_phone(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.phone)))


    def name_input(self):
        self.get_name().send_keys(fake.name())

    def email_input(self):
        self.get_email().send_keys(fake.email())

    def phone_input(self):
        self.get_phone().send_keys(fake.numerify(text='913 %%%-%%-%%'))





