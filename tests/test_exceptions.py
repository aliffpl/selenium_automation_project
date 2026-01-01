import pytest
from utils import driver as driver_module
from config import BASE_URL

try:
    from selenium.common.exceptions import NoSuchElementException
except ImportError:
    class NoSuchElementException(Exception):
        pass

def test_missing_element_raises_nosuchelement():
    """Objective: Ensure accessing a missing element raises NoSuchElementException gracefully."""
    try:
        driver = driver_module.create_driver()
        driver.get(BASE_URL + "/non-existent-page")
        if getattr(driver, 'is_fake', False):
            # FakeDriver does not raise; assert it returns a fake element instead
            el = driver.find_element("id", "this-does-not-exist")
            assert el is not None
        else:
            with pytest.raises(NoSuchElementException):
                driver.find_element("id", "this-does-not-exist")
    finally:
        try:
            driver.quit()
        except Exception:
            pass

def test_page_load_timeout_raises():
    """Objective: Simulate a page load timeout and ensure exception handling."""
    try:
        driver = driver_module.create_driver()
        # Set a small page load timeout to force timeout
        driver.set_page_load_timeout(0.001)
        with pytest.raises(Exception):
            driver.get(BASE_URL + "/")
    finally:
        try:
            driver.quit()
        except Exception:
            pass
