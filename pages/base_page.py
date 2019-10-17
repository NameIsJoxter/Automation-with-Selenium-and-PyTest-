import math
from selenium.common.exceptions import NoAlertPresentException

class BasePage():

    def __init__(self, driver, url, timeout=5):
        self.driver = driver
        self.driver.implicitly_wait(timeout)
        self.url = url

    def is_element_present(self, how, what):
        try:
            self.driver.find_element(how, what)
        except Exception:
            return False
        return True

    def open(self):
        self.driver.get(self.url)

    def solve_quiz_and_get_code(self):
        alert = self.driver.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.driver.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")