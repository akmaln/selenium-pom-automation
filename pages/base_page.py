from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

class BasePage:
    def __init__(self, driver, timeout = 10):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    def click(self, locator):
        self.wait.until(EC.element_to_be_clickable(locator)).click()

    def find(self, locator):
        return self.wait.until(EC.presence_of_element_located(locator))

    def enter_text(self, locator, text):
        self.wait.until(EC.element_to_be_clickable(locator)).send_keys(text)

    def is_present(self, locator):
        try:
            self.wait.until(EC.presence_of_element_located(locator))
            return True
        except TimeoutException:
            return False
