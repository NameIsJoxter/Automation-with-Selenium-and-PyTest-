import time
import pytest
from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.basket_page import BasketPage

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"


class TestLoginFromMainPage():
    def test_guest_can_go_to_login_page(self, driver):
        page = MainPage(driver, link)
        page.open()
        page.go_to_login_page()
        login_page = LoginPage(driver, driver.current_url)
        login_page.should_be_login_page()

    def test_guest_can_see_login_link(self, driver):
        page = MainPage(driver, link)
        page.open()


def test_guest_cant_see_product_in_basket_opened_from_main_page(driver):
    page = MainPage(driver, link)
    page.open()
    page.go_to_basket_page()
    basket_page = BasketPage(driver, driver.current_url)
    basket_page.should_be_promo_in_empty_basket()
    basket_page.should_not_be_basket_items()
