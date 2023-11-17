'''Тестируется покупка пылесоса на сайте kuvalda.ru'''

from selenium.webdriver.chrome.options import Options
from pages.mainPage import *
from pages.cart_Page import *
from pages.deliveryMethod_Page import *
from pages.personalData_Page import *
import allure

options = Options()
options.page_load_strategy = 'eager'
options.add_experimental_option('excludeSwitches', ['enable-logging'])

@allure.description("Test buy product")
def test_buy_product(set_up):
    driver = webdriver.Chrome(options=options)
    '''Главная страница'''
    mp=Main_Page(driver)
    mp.ShowMainPage_and_CheckURL()
    '''Страница корзины'''
    cp=Cart_Page(driver)
    cp.cart()
    cp.assert_cart(SELECTED_PRODUCT,CART_PRODUCT)
    cp.click_order()
    '''Страница заполнения персональных данных'''
    pd=PersonalData_Page(driver)
    time.sleep(2)
    pd.input_personal_data()

    '''Страница выбора способа доставки'''
    dp = DeliveryMethod_Page(driver)
    time.sleep(2)
    dp.input_delivery_data()
    time.sleep(3)
    '''Подтверждение заказа и переход к оплате'''
    dp.click_confirm_button()
    time.sleep(5)

    '''Подтверждение - скриншот'''
    dp.make_screenshot()

    time.sleep(10)










