
def test_remove_checkbox(dynamic_controls):

    dynamic_controls.click_remove()
    dynamic_controls.wait_for_loading()

    assert not dynamic_controls.is_checkbox_present(), "checkbox is present"

def test_add_checkbox(dynamic_controls):

    dynamic_controls.click_remove()
    dynamic_controls.click_add()

    assert dynamic_controls.is_checkbox_present(), "checkbox isnt present"

def test_enable_input(dynamic_controls):

    dynamic_controls.click_enable()
    dynamic_controls.wait_for_loading()

    assert dynamic_controls.is_input_enabled(), "input is not enabled"

def test_enable_and_type_input(dynamic_controls):

    dynamic_controls.click_enable()
    dynamic_controls.type_in_input("hello")

    assert dynamic_controls.get_input_value() == "hello", "no text in input field"

