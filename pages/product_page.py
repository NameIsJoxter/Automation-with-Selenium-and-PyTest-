from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):

    def add_to_basket(self):
        self.should_be_add_to_basket_btn()
        self.add_to_basket()

    def should_be_add_to_basket_btn(self):
        assert self.is_element_present(*ProductPageLocators.ADD_TO_BASKET_BTN), 'There is no add to basket button at the page'

    def add_to_basket(self):
        btn = self.driver.find_element(*ProductPageLocators.ADD_TO_BASKET_BTN)
        btn.click()