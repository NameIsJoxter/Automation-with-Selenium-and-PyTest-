from .base_page import BasePage
from .locators import BasePageLocators, ProductPageLocators


class ProductPage(BasePage):
    def go_to_basket_page(self):
        link = self.driver.find_element(*BasePageLocators.BASKET_BTN)
        link.click()

    def press_add_to_basket_btn(self):
        btn = self.driver.find_element(*ProductPageLocators.ADD_TO_BASKET_BTN)
        btn.click()

    def should_be_add_to_basket_btn(self):
        assert self.is_element_present(*ProductPageLocators.ADD_TO_BASKET_BTN), 'Add to basket button is not presented'

    def should_be_message_about_adding(self):
        assert self.is_element_present(*ProductPageLocators.ADDED_PRODUCT_NAME_POPUP), 'Product name allert is not presented'

    def should_be_message_basket_total(self):
        assert self.is_element_present(*ProductPageLocators.BASKET_TOTAL_POPUP), 'Product name allert is not presented'

    def should_desappear_message_about_adding(self):
        assert self.is_disappeared(*ProductPageLocators.ADDED_PRODUCT_NAME_POPUP), 'Success message hasnt desappear, but it should'

    def should_not_be_message_about_adding(self):
        assert self.is_not_element_present(*ProductPageLocators.ADDED_PRODUCT_NAME_POPUP),'Success message is presented, but should not be'

    def product_name_should_be_present_in_success_message(self):
        product_name = self.driver.find_element(*ProductPageLocators.PRODUCT_NAME)
        product_name_in_message = self.driver.find_element(*ProductPageLocators.ADDED_PRODUCT_NAME_POPUP)
        assert product_name.text in product_name_in_message.text, 'Wrong product name in message'

    def product_cost_should_be_equal_basket_total_in_success_message(self):
        product_cost = self.driver.find_element(*ProductPageLocators.PRODUCT_COST)
        basket_total_in_message = self.driver.find_element(*ProductPageLocators.BASKET_TOTAL_POPUP)
        assert product_cost.text in basket_total_in_message.text, 'Wrong cost in message'
