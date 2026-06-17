from pages.dropdown_page import DropdownPage
import pytest

@pytest.mark.parametrize("option", ["Option 1", "Option 2"])
def test_dropdown(driver, option):
    dropdown_page = DropdownPage(driver)

    dropdown_page.open()

    dropdown_page.select_an_option(option)

    assert dropdown_page.currently_selected_option() == option, f"Expected {option} to be selected"
