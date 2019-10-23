from faker import Faker
import pytest
from pages.product_page import ProductPage
from pages.login_page import LoginPage
from pages.basket_page import BasketPage

f = Faker()

email = f.email()
password = f.password()
link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019'


class TestGuestAddToBasketFromProductPage():
    @pytest.mark.need_review
    def test_guest_can_add_product_to_basket(self, driver):
        page = ProductPage(driver, link)
        page.open()
        page.should_be_add_to_basket_btn()
        page.press_add_to_basket_btn()
        page.solve_quiz_and_get_code()
        page.should_be_message_about_adding()
        page.product_name_should_be_present_in_success_message()
        page.should_be_message_basket_total()
        page.product_cost_should_be_equal_basket_total_in_success_message()

    @pytest.mark.xfail
    def test_guest_cant_see_success_message_after_adding_product_to_basket(self, driver):
        page = ProductPage(driver, link)
        page.open()
        page.press_add_to_basket_btn()
        page.solve_quiz_and_get_code()
        page.should_not_be_message_about_adding()

    def test_guest_cant_see_success_message(self, driver):
        page = ProductPage(driver, link)
        page.open()
        page.should_not_be_message_about_adding()

    @pytest.mark.xfail
    def test_message_disappeared_after_adding_product_to_basket(self, driver):
        page = ProductPage(driver, link)
        page.open()
        page.press_add_to_basket_btn()
        page.solve_quiz_and_get_code()
        page.should_desappear_message_about_adding()


class TestUserAddToBasketFromProductPage:
    @pytest.fixture(scope='function')
    def test_setup(self, driver):
        page = LoginPage(driver, 'http://selenium1py.pythonanywhere.com/ru/accounts/login/')    # WTD get rid of hardcoded link
        page.open()
        page.register_new_user(email, password)
        page.should_be_autorized_user()

    def test_user_cant_see_success_message(self, driver):
        page = ProductPage(driver, link)
        page.open()
        page.should_not_be_message_about_adding()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, driver):
        page = ProductPage(driver, link)
        page.open()
        page.should_be_add_to_basket_btn()
        page.press_add_to_basket_btn()
        page.solve_quiz_and_get_code()
        page.should_be_message_about_adding()
        page.product_name_should_be_present_in_success_message()
        page.should_be_message_basket_total()
        page.product_cost_should_be_equal_basket_total_in_success_message()


@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(driver):
    page = ProductPage(driver, link)
    page.open()
    page.should_be_login_link()
    page.go_to_login_page()
    login_page = LoginPage(driver, driver.current_url)
    login_page.should_be_login_page()
    login_page.should_be_login_form()
    login_page.should_be_register_form()


@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(driver):
    page = ProductPage(driver, link)
    page.open()
    page.go_to_basket_page()
    basket_page = BasketPage(driver, driver.current_url)
    basket_page.should_be_promo_in_empty_basket()
    basket_page.should_not_be_basket_items()
