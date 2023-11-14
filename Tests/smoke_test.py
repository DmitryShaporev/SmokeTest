
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from Pages import mainPage
options = Options()
options.page_load_strategy = 'eager'

def test_buy_product():
    driver = webdriver.Chrome(options=options)
    print('Start Test')
    mp=mainPage.Main_Page(driver)
    mp.ShowMainPage_and_CheckURL()
    time.sleep(10)







