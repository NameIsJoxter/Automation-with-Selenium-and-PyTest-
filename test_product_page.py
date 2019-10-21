import pytest
import time
from pages.product_page import ProductPage
from pages.login_page import LoginPage

link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019'

# @pytest.mark.parametrize('promo_code', [0, 1, 2, 3, 4, 5, 6, pytest.param(7, marks=pytest.mark.xfail), 8, 9])
@pytest.mark.skip
def test_guest_can_add_product_to_basket(driver):
    page = ProductPage(driver, link)
    page.open()
    page.should_be_add_to_basket_btn()
    page.press_add_to_basket_btn()
    page.solve_quiz_and_get_code()
    page.should_be_message_about_adding()
    page.product_name_should_be_present_in_success_message()
    page.should_be_message_basket_total()
    page.product_cost_should_be_equal_basket_total_in_success_message()
    # time.sleep(10)

@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(driver):
    page = ProductPage(driver, link)
    page.open()
    page.press_add_to_basket_btn()
    page.solve_quiz_and_get_code()
    page.should_not_be_message_about_adding()

def test_guest_cant_see_success_message(driver):
    page = ProductPage(driver, link)
    page.open()
    page.should_not_be_message_about_adding()

@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(driver):
    page = ProductPage(driver, link)
    page.open()
    page.press_add_to_basket_btn()
    page.solve_quiz_and_get_code()
    time.sleep(1)
    page.should_desappear_message_about_adding()

def test_guest_can_go_to_login_page_from_product_page(driver):
    page = ProductPage(driver, link)
    page.open()
    page.should_be_login_link()
    page.go_to_login_page()
    login_page = LoginPage(driver, driver.current_url)
    login_page.should_be_login_page()
    login_page.should_be_login_form()
    login_page.should_be_register_form()