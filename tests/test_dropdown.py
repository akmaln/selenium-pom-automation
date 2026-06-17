
import pytest

@pytest.mark.parametrize("option", ["Option 1", "Option 2"])
def test_dropdown(dropdown, option):

    dropdown.select_an_option(option)

    assert dropdown.currently_selected_option() == option, f"Expected {option} to be selected"
