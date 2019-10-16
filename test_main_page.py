from pages.main_page import MainPage
from pages.login_page import LoginPage

def test_guest_can_go_to_login_page(driver):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(driver, link)
    page.open()
    page.should_be_login_link()
    page.go_to_login_page()
    login_page = LoginPage(driver, driver.current_url)
    login_page.should_be_login_page()
    login_page.should_be_login_form()
    login_page.should_be_register_form()