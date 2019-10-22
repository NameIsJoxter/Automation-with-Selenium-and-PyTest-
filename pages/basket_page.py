from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_be_promo_in_empty_basket(self):
        assert self.is_element_present(*BasketPageLocators.EMPTY_BASKET_MESSAGE), 'There is no promo at the empty basket'

        promo_text = self.driver.find_element(*BasketPageLocators.EMPTY_BASKET_MESSAGE).text
        expected_promo_text = 'Your basket is empty. Continue shopping'     # WTD: get rid of hardcode for en-gb
        assert promo_text == expected_promo_text, 'Promo text at the empty page is not correct'

    def should_not_be_basket_items(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEMS), 'There are items in empty basket'
