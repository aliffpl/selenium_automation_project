import pytest
from utils import driver as driver_module
from pages.form_page import TextBoxPage
from config import BASE_URL

def test_input_field_constraints_and_placeholders():
    """Objective: Verify input fields exist, have expected attributes and are interactable."""
    try:
        driver = driver_module.create_driver()
        page = TextBoxPage(driver, BASE_URL)
        page.open()
        name_el = driver.find_element(*page.INPUT_FULL_NAME)
        email_el = driver.find_element(*page.INPUT_EMAIL)
        assert name_el.is_enabled(), "Name input should be enabled"
        assert email_el.get_attribute('placeholder') is not None
        assert name_el.get_attribute('id') == 'userName'
    except RuntimeError as e:
        pytest.skip(str(e))
    finally:
        try:
            driver.quit()
        except Exception:
            pass
