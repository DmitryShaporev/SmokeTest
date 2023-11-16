import pytest
from selenium.webdriver.chrome.options import Options
from pages.mainPage import *
from pages.cart_Page import *
from pages.base_page import *
from pages.order_Page import *

options = Options()
options.page_load_strategy = 'eager'
options.add_experimental_option('excludeSwitches', ['enable-logging'])

@pytest.fixture(scope="module")
def set_up():
    print("\nНачало тестирования")
    yield
    print("\nТестирование закончено")

def test_buy_product(set_up):
    driver = webdriver.Chrome(options=options)
    mp=Main_Page(driver)
    mp.ShowMainPage_and_CheckURL()
    cp=Cart_Page(driver)
    cp.cart()
    cp.assert_cart(SELECTED_PRODUCT,CART_PRODUCT)
    cp.click_order()
    op=Order_Page(driver)
    op.name_input()
    op.email_input()
    op.phone_input()
    time.sleep(10)










