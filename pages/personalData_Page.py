from faker import Faker
from pages.base_page import *

fake=Faker()
class PersonalData_Page(BasePage):

    def __init__(self,driver):
        super().__init__(driver)
        self.driver=driver


        # locators
    name="//input[@id='checkout_1']"
    email="//input[@id='checkout_2']"
    phone="//input[@id='checkout_3']"
    next_button="//button[@class='form__submit form__submit_no-fluid button']"

        #getters
    def get_name(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.name)))

    def get_email(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.email)))

    def get_phone(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.phone)))

    def get_next_button(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.next_button)))

    def name_input(self):
        self.get_name().send_keys(fake.name())

    def email_input(self):
        self.get_email().send_keys(fake.email())

    def phone_input(self):
        self.get_phone().send_keys(fake.numerify(text='913 %%%-%%-%%'))

    def click_next_button(self):
        self.get_next_button().click()

    def input_personal_data(self):
        self.name_input()
        self.email_input()
        self.phone_input()
        self.click_next_button()






