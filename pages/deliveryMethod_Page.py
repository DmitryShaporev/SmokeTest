import allure
from faker import Faker
from pages.base_page import *
from utilities.logger import Logger

fake=Faker()
class DeliveryMethod_Page(BasePage):

    def __init__(self,driver):
        super().__init__(driver)
        self.driver=driver


        # locators
    courier_button="//button[@class='checkout__tab']"
    city="//input[@id='address_0']"
    street="//input[@id='address_1']"
    home = "//input[@id='address_2']"
    other_deliver="//input[@id='delivery[deliveryOther]']"
    next_button='//button[@class="form__submit button"]'
    confirm_button="//button[@class='checkout-submit__submit button button_fluid']"

        #getters
    def get_courier_button(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.courier_button)))

    def get_city(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.city)))

    def get_street(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.street)))

    def get_home(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.home)))

    def get_other_deliver(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.other_deliver)))

    def get_next_button(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.next_button)))

    def get_confirm_button(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.confirm_button)))

    #actions
    def click_courier_button(self):
        self.get_courier_button().click()

    def city_input(self):
        self.get_city().send_keys(fake.city())

    def street_input(self):
        self.get_street().send_keys(fake.street_name())

    def home_input(self):
        self.get_home().send_keys('25')

    def click_other_deliver(self):
        self.get_other_deliver().send_keys(fake.company())

    def click_next_button(self):
        self.get_next_button().click()

    def click_confirm_button(self):
        self.get_confirm_button().click()

    def input_delivery_data(self):
        Logger.add_start_step(method="input_delivery_data")
        self.click_courier_button()
        self.city_input()
        self.street_input()
        self.home_input()

        self.click_next_button()
        self.click_other_deliver()
        self.click_next_button()
        Logger.add_end_step(url=self.driver.current_url, method="input_delivery_data")

    def confirm_order(self):
        with allure.step("Подтверждение заказ. Переход на страницу оплаты"):
            Logger.add_start_step(method="input_delivery_data")
            self.click_confirm_button()
            Logger.add_end_step(url=self.driver.current_url, method="input_delivery_data")







