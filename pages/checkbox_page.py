from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CheckboxPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open(self):
        self.driver.get("https://the-internet.herokuapp.com/checkboxes")

    def click_checkbox(self, number):
        self.wait.until(EC.element_to_be_clickable((By.XPATH, f"//form[@id='checkboxes']/input[{number}]"))).click()

    def checkbox_is_selected(self, number):
        return self.wait.until(EC.element_to_be_clickable((By.XPATH, f"//form[@id='checkboxes']/input[{number}]"))).is_selected()
