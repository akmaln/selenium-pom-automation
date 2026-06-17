
import pytest

@pytest.mark.parametrize("number, expected", [(1, False),(2, True)])
def test_checkbox(checkboxes, number, expected):

    assert checkboxes.checkbox_is_selected(number) == expected, f"checkbox {number} should be unchecked by default"

@pytest.mark.parametrize("number, expected", [(1, True),(2, False)])
def test_checkbox_becomes_checked_after_click(checkboxes, number, expected):

    checkboxes.click_checkbox(number)
    assert checkboxes.checkbox_is_selected(number) == expected, f"checkbox {number} is not selected"
