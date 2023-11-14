import random
import time

from selenium.webdriver.common.by import By
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Pages.base_page import BasePage



class Main_Page(BasePage):
    url = 'https://www.kuvalda.ru/'
    def __init__(self,driver):
        super().__init__(driver)
        self.driver=driver

    #Locators
    catalog="//button[@class='main-header__catalog button']"
    menu_item="//span[contains(text(), 'Клининг')]"
    submenu_item="//a[contains(text(), 'Пылесосы')]"
    def brandlist(self):
        brands=WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.catalog)))
        print(brands)

    #getters
    '''получаем локатор кнопки каталога'''
    def get_catalog(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.catalog)))
    '''получаем локатор пункта меню'''
    def get_memu_item(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.menu_item)))
    '''получаем локатор пункта подменю'''
    def get_submemu_item(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.submenu_item)))


    #actions

    def click_catalog(self):
        self.get_catalog().click()
    def hover_menu_item(self):
        ActionChains(self.driver).move_to_element(self.get_memu_item()).perform()

    def click_submenu_item(self):
        self.get_submemu_item().click()
    def brandlist(self):

        brands=self.driver.find_elements(By.XPATH,"//div[@class='filter__option']")

        blist=[]
        for item in brands:
            blist.append(item.text)
        print(blist)
        brands_only = [item for item in blist if item.isupper()]
        print(brands_only)
        random_elements = random.sample(brands_only, 2)
        print(random_elements)


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
        self.brandlist()

        '''Проверка перехода на нужную страницу'''
        self.assert_url('https://www.kuvalda.ru/catalog/1939/')


        #self.assert_url("https://www.mvideo.ru/televizory-i-cifrovoe-tv-1/televizory-65?from=under_search")








