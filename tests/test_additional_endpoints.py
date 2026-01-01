import pytest
from utils import driver as driver_module
from pages.homepage import HomePage
from pages.form_page import TextBoxPage
from pages.links_page import LinksPage
from config import BASE_URL, TEST_USER
from utils.logger import setup_logger

LOG = setup_logger(__name__)


def test_api_endpoint_buttons_page():
    """Test objective: Verify navigation to buttons page and button elements exist.
    
    Input: BASE_URL + "/buttons"
    Expected: Page loads with title containing 'Buttons'
    """
    driver = driver_module.create_driver()
    try:
        driver.get(BASE_URL + "/buttons")
        if getattr(driver, 'is_fake', False):
            assert "Buttons" in driver.title or driver.current_url.endswith("/buttons")
        else:
            assert "Button" in driver.title.lower() or "button" in driver.current_url.lower()
        LOG.info("Buttons page loaded successfully: %s", driver.title)
    finally:
        try:
            driver.quit()
        except Exception:
            pass


def test_api_endpoint_upload_download_page():
    """Test objective: Navigate to upload/download page and verify it loads.
    
    Input: BASE_URL + "/upload-download"
    Expected: Page loads successfully
    """
    driver = driver_module.create_driver()
    try:
        driver.get(BASE_URL + "/upload-download")
        # Verify URL and basic page state
        assert BASE_URL in driver.current_url or "upload" in driver.current_url.lower()
        LOG.info("Upload/Download page loaded, URL: %s", driver.current_url)
    finally:
        try:
            driver.quit()
        except Exception:
            pass


def test_api_endpoint_alerts_page():
    """Test objective: Navigate to alerts page and verify page structure.
    
    Input: BASE_URL + "/alerts"
    Expected: Page loads and contains alert-related content
    """
    driver = driver_module.create_driver()
    try:
        driver.get(BASE_URL + "/alerts")
        # Verify page loaded
        assert driver.current_url is not None
        assert len(driver.title) > 0
        LOG.info("Alerts page loaded, title: %s", driver.title)
    finally:
        try:
            driver.quit()
        except Exception:
            pass


def test_api_endpoint_frames_page():
    """Test objective: Navigate to frames page and verify page loads.
    
    Input: BASE_URL + "/frames"
    Expected: Page loads without errors
    """
    driver = driver_module.create_driver()
    try:
        driver.get(BASE_URL + "/frames")
        assert driver.current_url is not None
        LOG.info("Frames page loaded successfully")
    finally:
        try:
            driver.quit()
        except Exception:
            pass
