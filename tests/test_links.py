import pytest
from utils import driver as driver_module
from pages.links_page import LinksPage
from config import BASE_URL

def test_links_href_and_click():
    """Objective: Verify link href attribute and clicking behavior."""
    driver = driver_module.create_driver()
    try:
        page = LinksPage(driver, BASE_URL)
        page.open()
        href = page.get_simple_link_href()
        assert href is not None and href.startswith('http'), "Simple link should have an absolute href"
        # clicking should not raise in FakeDriver; ensure current_url unchanged or updated in real driver
        page.click_simple_link()
        # If fake driver, clicking does nothing; if real, ensure navigation occurred
        if getattr(driver, 'is_fake', False):
            assert driver.current_url.endswith('/links')
        else:
            assert 'demoqa' in driver.current_url
    finally:
        try:
            driver.quit()
        except Exception:
            pass
