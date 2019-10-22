import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def pytest_addoption(parser):
    parser.addoption('--language', action='store',default='en',help='Choose language: es, fr, etc')

@pytest.fixture(scope="function")
def driver(request):
    user_language = request.config.getoption('language')
    options = Options()
    options.add_experimental_option('prefs',{'intl.accept_languages': user_language})
    print(f"\nStart browser for test, {user_language} language")
    driver = webdriver.Chrome(options=options)
    yield driver
    print("\nquit browser..")
    driver.quit()
