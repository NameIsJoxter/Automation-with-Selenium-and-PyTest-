from pages.product_page import ProductPage
import time

def test_guest_can_add_product_to_basket(driver):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019'
    page = ProductPage(driver, link)
    page.open()
    page.should_be_add_to_basket_btn()
    page.press_add_to_basket_btn()
    page.solve_quiz_and_get_code()
    page.should_be_message_about_adding()
    page.should_be_message_basket_total()
    # time.sleep(30000)