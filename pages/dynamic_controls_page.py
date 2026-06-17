from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

class DynamicControlsPage:

    REMOVE_BUTTON = (By.XPATH, "//button[text()='Remove']")
    ADD_BUTTON = (By.XPATH, "//button[text()='Add']")
    CHECKBOX = (By.ID, "checkbox")
    INPUT_FIELD = (By.CSS_SELECTOR, "#input-example input")
    ENABLE_BUTTON = (By.XPATH, "//button[text()='Enable']")
    DISABLE_BUTTON = (By.XPATH, "//button[text()='Disable']")


    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open(self):
        self.driver.get("https://the-internet.herokuapp.com/dynamic_controls")

    def click_remove(self):
        self.wait.until(EC.element_to_be_clickable(self.REMOVE_BUTTON)).click()

    def click_add(self):
        self.wait.until(EC.element_to_be_clickable(self.ADD_BUTTON)).click()

    def click_enable(self):
        self.wait.until(EC.element_to_be_clickable(self.ENABLE_BUTTON)).click()

    def click_disable(self):
        self.wait.until(EC.element_to_be_clickable(self.DISABLE_BUTTON)).click()

    def is_checkbox_present(self):
        try:
            self.wait.until(EC.presence_of_element_located(self.CHECKBOX))
            return True
        except TimeoutException:
            return False

    def is_input_enabled(self):
        return self.wait.until(EC.presence_of_element_located(self.INPUT_FIELD)).is_enabled()

    def type_in_input(self, text):
        self.wait.until(EC.element_to_be_clickable(self.INPUT_FIELD)).send_keys(text)

    def get_input_value(self):
        return self.wait.until(EC.presence_of_element_located(self.INPUT_FIELD)).get_attribute("value")

    def wait_for_loading(self):
        self.wait.until(EC.invisibility_of_element_located((By.ID, "loading")))
