from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage

class DynamicControlsPage(BasePage):

    REMOVE_BUTTON = (By.XPATH, "//button[text()='Remove']")
    ADD_BUTTON = (By.XPATH, "//button[text()='Add']")
    CHECKBOX = (By.ID, "checkbox")
    INPUT_FIELD = (By.CSS_SELECTOR, "#input-example input")
    ENABLE_BUTTON = (By.XPATH, "//button[text()='Enable']")
    DISABLE_BUTTON = (By.XPATH, "//button[text()='Disable']")

    def open(self):
        self.driver.get("https://the-internet.herokuapp.com/dynamic_controls")

    def click_remove(self):
        self.click(self.REMOVE_BUTTON)

    def click_add(self):
        self.click(self.ADD_BUTTON)

    def click_enable(self):
        self.click(self.ENABLE_BUTTON)

    def click_disable(self):
        self.click(self.DISABLE_BUTTON)

    def is_checkbox_present(self):
        return self.is_present(self.CHECKBOX)

    def is_input_enabled(self):
        return self.find(self.INPUT_FIELD).is_enabled()

    def type_in_input(self, text):
        self.enter_text(self.INPUT_FIELD, text)

    def get_input_value(self):
        return self.find(self.INPUT_FIELD).get_attribute("value")

    def wait_for_loading(self):
        self.wait.until(EC.invisibility_of_element_located((By.ID, "loading")))
