from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class DropdownPage:
    DROPDOWN_LIST = (By.ID, "dropdown")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open(self):
        self.driver.get("https://the-internet.herokuapp.com/dropdown")

    def select_an_option(self, option_text):
        element = self.wait.until(EC.element_to_be_clickable(self.DROPDOWN_LIST))
        dropdown = Select(element)
        dropdown.select_by_visible_text(option_text)

    def currently_selected_option(self):
        element = self.wait.until(EC.element_to_be_clickable(self.DROPDOWN_LIST))
        dropdown = Select(element)
        return dropdown.first_selected_option.text
