
from .base_page import BasePage
from .locators import ProductPageLocators
from selenium.webdriver.support import expected_conditions as ec

class ProductPage(BasePage):

    def add_to_basket(self):
        self.should_be_add_to_basket_btn()
        self.add_product_to_basket()

    def should_be_add_to_basket_btn(self):
        assert self.is_element_present(*ProductPageLocators.ADD_TO_BASKET_BTN), 'There is no add to basket button at the product page'

    def add_product_to_basket(self):
        btn = self.driver.find_element(*ProductPageLocators.ADD_TO_BASKET_BTN)
        btn.click()

    # def should_be_add_to_basket_popups(self):
    #     popups = self.driver.find_elements(*ProductPageLocators.POPUPS)
    #     assert len(popups) > 0, 'There are no success popups at the product page'