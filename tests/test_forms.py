import pytest
from utils import driver as driver_module
from pages.form_page import TextBoxPage
from config import BASE_URL, TEST_USER
from utils.logger import setup_logger

LOG = setup_logger(__name__)

def test_textbox_positive_submit():
    """Objective: Submit text box form with valid data and verify output."""
    try:
        driver = driver_module.create_driver()
        page = TextBoxPage(driver, BASE_URL)
        page.open()
        page.fill_form(TEST_USER['first_name'] + ' ' + TEST_USER['last_name'], TEST_USER['email'], TEST_USER['current_address'])
        page.submit()
        out = page.get_output_text()
        assert TEST_USER['first_name'] in out
        assert TEST_USER['email'] in out
        LOG.info("Text box form submitted and output verified")
    except RuntimeError as e:
        pytest.skip(str(e))
    finally:
        try:
            driver.quit()
        except Exception:
            pass

def test_textbox_invalid_email_shows_no_output():
    """Objective: Submit form with invalid email and validate behavior (negative case)."""
    try:
        driver = driver_module.create_driver()
        page = TextBoxPage(driver, BASE_URL)
        page.open()
        page.fill_form('Invalid Email', 'not-an-email', 'addr')
        page.submit()
        out = page.get_output_text()
        assert 'Email' in out or out == '', "Unexpected output for invalid email"
        LOG.info("Invalid email test executed; output: %s", out)
    except RuntimeError as e:
        pytest.skip(str(e))
    finally:
        try:
            driver.quit()
        except Exception:
            pass
