from .base_page import BasePage
from .locators import BasePageLocators

class MainPage(BasePage):
    def go_to_basket_page(self):
        link = self.driver.find_element(*BasePageLocators.BASKET_BTN)
        link.click()