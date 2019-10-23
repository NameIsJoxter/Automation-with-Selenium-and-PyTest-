from selenium.webdriver.common.by import By
from selenium import webdriver
driver = webdriver.Chrome


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, '#login_link')
    BASKET_BTN = (By.CSS_SELECTOR, '.btn-group .btn')
    USER_ICON = (By.CSS_SELECTOR, '.icon-user')


class BasketPageLocators:
    BASKET_URL = (driver.current_url, 'http://selenium1py.pythonanywhere.com/en-gb/basket/')        # WTD: get rid of hardcode for en-gb
    BASKET_ITEMS = (By.CSS_SELECTOR,'.basket-items')
    EMPTY_BASKET_MESSAGE = (By.CSS_SELECTOR, '#content_inner > p')


class LoginPageLocators:
    LOGIN_URL = (driver.current_url, 'http://selenium1py.pythonanywhere.com/en-gb/accounts/login/')     # WTD: get rid of hardcode for en-gb
    LOGIN_FORM = (By.CSS_SELECTOR, '#login_form')
    REGISTER_FORM = (By.CSS_SELECTOR, '#register_form')
    EMAIL_REGISTRATION = (By.CSS_SELECTOR, '#id_registration-email')
    PASSWORD_REGISTRATION = (By.CSS_SELECTOR, '#id_registration-password1')
    PASSWORD_REGISTRATION_CONFIRM = (By.CSS_SELECTOR, '#id_registration-password2')
    REGISTER_BUTTON = (By.CSS_SELECTOR, '[name=registration_submit]')

class ProductPageLocators:
    PRODUCT_NAME = (By.CSS_SELECTOR, '.product_main h1')
    PRODUCT_COST = (By.CSS_SELECTOR, '.price_color')
    ADD_TO_BASKET_BTN = (By.CSS_SELECTOR, '.btn-add-to-basket')
    ADDED_PRODUCT_NAME_POPUP = (By.XPATH,'//*[@id = "messages"]/*[1]//strong')
    BASKET_TOTAL_POPUP = (By.XPATH, '//*[@id = "messages"]/*[3]//strong')
