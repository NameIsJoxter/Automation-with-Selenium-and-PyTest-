from .base_page import BasePage
from .locators import MainPageLocators

class MainPage(BasePage):
    def go_to_basket_page(self):
        link = self.driver.find_element(*MainPageLocators.BASKET_LINK)
        link.click()