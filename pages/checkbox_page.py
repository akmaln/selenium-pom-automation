from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class CheckboxPage(BasePage):

    def open(self):
        self.driver.get("https://the-internet.herokuapp.com/checkboxes")

    def _checkbox(self, number):
        return By.XPATH, f"//form[@id='checkboxes']/input[{number}]"

    def click_checkbox(self, number):
        self.click(self._checkbox(number))

    def checkbox_is_selected(self, number):
        return self.find(self._checkbox(number)).is_selected()
