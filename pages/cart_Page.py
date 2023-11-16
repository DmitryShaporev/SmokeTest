
from pages.base_page import *


class Cart_Page(BasePage):

    def __init__(self,driver):
        super().__init__(driver)
        self.driver=driver


        # locators
    product_title="//a[@class='cart-snippet__title link']"
    product_price="//div[@class='cart-snippet__total-value']"
    order_button="//a[@class='cart__submit button button_fluid']"

        #getters
    def get_product_title(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.product_title)))

    def get_product_price(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.product_price)))

    def get_order_button(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.order_button)))


    def check_cart(self):
        time.sleep(3)
        CART_PRODUCT.append(self.get_product_title().text)
        CART_PRODUCT.append(self.get_product_price().text[:-2])


    def cart(self):
        self.check_cart()

    def click_order(self):
        self.get_order_button().click()




