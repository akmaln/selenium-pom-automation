from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from pages.base_page import BasePage

class DropdownPage(BasePage):
    DROPDOWN_LIST = (By.ID, "dropdown")

    def open(self):
        self.driver.get("https://the-internet.herokuapp.com/dropdown")

    def select_an_option(self, option_text):
        element = self.find(self.DROPDOWN_LIST)
        dropdown = Select(element)
        dropdown.select_by_visible_text(option_text)

    def currently_selected_option(self):
        element = self.find(self.DROPDOWN_LIST)
        dropdown = Select(element)
        return dropdown.first_selected_option.text
