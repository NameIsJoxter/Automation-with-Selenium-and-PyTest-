
from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):

    def test_guest_can_add_product_to_basket(self):
        self.should_be_add_to_basket_btn()
        self.press_add_to_basket_btn()
        self.should_be_message_about_adding()
        self.should_be_message_basket_total()

    def should_be_add_to_basket_btn(self):
        assert self.is_element_present(*ProductPageLocators.ADD_TO_BASKET_BTN), 'There is no add to basket button at the product page'

    def press_add_to_basket_btn(self):
        btn = self.driver.find_element(*ProductPageLocators.ADD_TO_BASKET_BTN)
        btn.click()

    def should_be_message_about_adding(self):
        assert self.is_element_present(*ProductPageLocators.ADDED_PRODUCT_NAME_POPUP), 'Product name allert is not presented'
        product_name = self.driver.find_element(*ProductPageLocators.PRODUCT_NAME).text
        product_name_in_message = self.driver.find_element(*ProductPageLocators.ADDED_PRODUCT_NAME_POPUP).text
        assert product_name in product_name_in_message, 'Wrong product name in message'

    def should_be_message_basket_total(self):
        assert self.is_element_present(*ProductPageLocators.BASKET_TOTAL_POPUP), 'Product name allert is not presented'
        product_cost = self.driver.find_element(*ProductPageLocators.PRODUCT_COST).text
        basket_total_in_message = self.driver.find_element(*ProductPageLocators.BASKET_TOTAL_POPUP).text
        assert product_cost in basket_total_in_message, 'Wrong cost in message'