
from pages.base_page import *


class Main_Page(BasePage):
    url = 'https://www.kuvalda.ru/'
    def __init__(self,driver):
        super().__init__(driver)
        self.driver=driver
        # self.SELECTED_PRODUCT=[]

    #Locators
    catalog="//button[@class='main-header__catalog button']" # локатор кнопки "Каталог"
    menu_item="//span[contains(text(), 'Клининг')]"          # локатор пункта меню
    submenu_item="//a[contains(text(), 'Пылесосы')]"         # локатор пункта подменю
    brand="//label[contains(text(), 'DAEWOO')]"               # локатор названия бренда DAEWOO
    tippy_box="//div[@class='tippy-box']"                    # локатор всплывающего окна
    show_ref="//a[contains(text(), 'Показать')]"             # ссылка "Показать"
    price_slider="/html/body/div[8]/div/div[1]/div/div[2]/form/div[2]/div[10]/div[1]" # локатор фильтра цен
    min_price = "//*[@id='filter_6125_min']"                   # локатор для ввода минимальной цены
    max_price = "//*[@id='filter_6125_max']"                   # локатор для ввода максимальной цены
    button_show = "//button[@class='filter__submit button']"   # кнопка "Показать"
    add_cart_button="//a[@class='alt-snippet__button button']" # кнопка "В корзину - добавдение товара в корзину"
    cart = "//a[@class='shop-service__wrapper link']"          # переход в корзину
    selected_title="//a[@class='alt-snippet__title link link_partial']" # название выбранного товара
    selected_price="//span[@class='alt-snippet__price-value']"          # цена выбранного товара

    #getters
    '''Кнопка каталога'''
    def get_catalog(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.catalog)))

    '''Пункт основного меню'''
    def get_memu_item(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.menu_item)))

    '''Пункт подменю'''
    def get_submemu_item(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.submenu_item)))

    '''Бренд (DAEWOO)'''
    def get_brand(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.brand)))

    '''Фильтр "Цена"'''
    def get_price_slider(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.price_slider)))

    '''Поле ввода минимальной цены'''
    def get_price_min(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.min_price)))

    '''Поле ввода максимальной цены'''
    def get_price_max(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.max_price)))

    '''Кнопка "Показать'''
    def get_button_show(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.button_show)))

    '''Кнопка добавления товара в корзину'''
    def get_cart_button(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.add_cart_button)))

    '''Переход на страницу корзины"'''
    def get_cart(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.cart)))

    def get_selected_title(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.selected_title)))

    def get_selected_price(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.selected_price)))

    #actions
    # переходим в каталог и соответствующие пункты меню
    def click_catalog(self):
        self.get_catalog().click()

    def hover_menu_item(self):
        ActionChains(self.driver).move_to_element(self.get_memu_item()).perform()

    def click_submenu_item(self):
        self.get_submemu_item().click()

    # Выбираем чекбокс с названиями брендов
    def click_brand(self):
       self.get_brand().click()
    # Получаем ссылку в сплывающем окне
    def show_refer(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.show_ref)))

    # переходим в фильтр цен и устанавлиыаем значения
    def click_price_slider(self):
        self.get_price_slider().click()

    def input_min_price(self):
        self.get_price_min().send_keys(10000)

    def input_max_price(self):
        self.get_price_max().send_keys(20000)

    def click_button_show(self):
        self.get_button_show().click()

    def click_cart_button(self):
        self.get_cart_button().click()

    def move_to_cart(self):
        self.get_cart().click()

    #methods

    def ShowMainPage_and_CheckURL(self):
        self.driver.maximize_window()
        self.driver.get(self.url)

        '''Открываем каталог товаров'''
        self.click_catalog()

        '''Наводим мышь на нужный пункт меню'''
        self.hover_menu_item()

        '''Клик по пункту подменю'''
        self.click_submenu_item()
        time.sleep(5)
        '''Проверка перехода на нужную страницу'''
        self.assert_url('https://www.kuvalda.ru/catalog/1939/')

        '''Выбираем  бренд'''
        self.click_brand()
        time.sleep(3)
        '''Клик на ссылку "Показать"'''
        self.show_refer().click()
        '''Клик на фильтр цен'''
        self.click_price_slider()
        self.input_min_price()
        self.input_max_price()
        '''Клик на кнопку Показать'''
        self.click_button_show()
        time.sleep(3)
        '''Получаем название и цену товара для последующего сравнения'''
        SELECTED_PRODUCT.append(self.get_selected_title().text)
        SELECTED_PRODUCT.append(self.get_selected_price().text)

        self.click_cart_button()
        '''Переходим в корзину'''
        self.move_to_cart()
















