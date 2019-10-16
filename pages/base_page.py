class BasePage():
    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.browser.implicitly_wait(timeout)
        self.url = url

    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except Exception:
            return False
        return True

    def open(self):
        self.browser.get(self.url)