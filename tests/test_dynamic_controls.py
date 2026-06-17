from pages.dynamic_controls_page import DynamicControlsPage

def test_remove_checkbox(driver):
    dynamic_control = DynamicControlsPage(driver)
    dynamic_control.open()

    dynamic_control.click_remove()
    dynamic_control.wait_for_loading()

    assert not dynamic_control.is_checkbox_present(), "checkbox is present"

def test_add_checkbox(driver):
    dynamic_control = DynamicControlsPage(driver)
    dynamic_control.open()

    dynamic_control.click_remove()
    dynamic_control.click_add()

    assert dynamic_control.is_checkbox_present(), "checkbox isnt present"

def test_enable_input(driver):
    dynamic_control = DynamicControlsPage(driver)
    dynamic_control.open()

    dynamic_control.click_enable()
    dynamic_control.wait_for_loading()

    assert dynamic_control.is_input_enabled(), "input is not enabled"

def test_enable_and_type_input(driver):
    dynamic_control = DynamicControlsPage(driver)
    dynamic_control.open()

    dynamic_control.click_enable()
    dynamic_control.type_in_input("hello")

    assert dynamic_control.get_input_value() == "hello", "no text in input field"

