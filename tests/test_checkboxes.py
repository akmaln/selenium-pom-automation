from pages.checkbox_page import CheckboxPage
import pytest

@pytest.mark.parametrize("number, expected", [(1, False),(2, True)])
def test_checkbox(driver, number, expected):
    checkboxes_page = CheckboxPage(driver)

    checkboxes_page.open()

    assert checkboxes_page.checkbox_is_selected(number) == expected, f"checkbox {number} should be unchecked by default"

@pytest.mark.parametrize("number, expected", [(1, True),(2, False)])
def test_checkbox_becomes_checked_after_click(driver, number, expected):
    checkboxes_page = CheckboxPage(driver)

    checkboxes_page.open()

    checkboxes_page.click_checkbox(number)
    assert checkboxes_page.checkbox_is_selected(number) == expected, f"checkbox {number} is not selected"
