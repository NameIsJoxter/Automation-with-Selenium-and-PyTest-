from selenium.webdriver.common.by import By
from selenium import webdriver
driver = webdriver.Chrome

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, '#login_link')

class LoginPageLocators():
    LOGIN_URL = (driver.current_url, 'http://selenium1py.pythonanywhere.com/en-gb/accounts/login/')
    LOGIN_FORM = (By.CSS_SELECTOR, '#login_form')
    REGISTER_FORM = (By.CSS_SELECTOR, '#register_form')

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, '#login_link')

class ProductPageLocators():
    PRODUCT_NAME = (By.CSS_SELECTOR, '.product_main h1')
    PRODUCT_COST = (By.CSS_SELECTOR, '.price_color')
    ADD_TO_BASKET_BTN = (By.CSS_SELECTOR, '.btn-add-to-basket')
    ADDED_PRODUCT_NAME_POPUP = (By.XPATH,'//*[@id = "messages"]/*[1]//strong')
    BASKET_TOTAL_POPUP = (By.XPATH, '//*[@id = "messages"]/*[3]//strong')