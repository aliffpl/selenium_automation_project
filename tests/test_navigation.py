import pytest
from utils import driver as driver_module
from pages.homepage import HomePage
from config import BASE_URL
from utils.logger import setup_logger

LOG = setup_logger(__name__)

def test_homepage_loads_and_title_and_url():
    """Test objective: Verify homepage loads, title and URL are correct.

    Steps:
    - Open homepage
    - Check title starts with expected string
    - Check current URL contains base URL

    Expected results:
    - Page title and URL match expectations
    """
    try:
        driver = driver_module.create_driver()
    except RuntimeError as e:
        pytest.skip(str(e))
    try:
        home = HomePage(driver)
        home.open()
        assert home.is_loaded(), "Homepage title does not match expected"
        assert BASE_URL in driver.current_url, "Current URL does not contain base URL"
        LOG.info("Homepage loaded successfully: %s", driver.title)
    finally:
        driver.quit()
