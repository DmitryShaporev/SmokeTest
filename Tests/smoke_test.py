
from selenium.webdriver.chrome.options import Options
from Pages.mainPage import *
from Pages.cart_Page import *
from Pages.base_page import *
options = Options()
options.page_load_strategy = 'eager'





def test_buy_product():
    driver = webdriver.Chrome(options=options)
    print('Start Test')
    mp=Main_Page(driver)
    mp.ShowMainPage_and_CheckURL()

    cp=Cart_Page(driver)
    cp.cart()





    time.sleep(10)










