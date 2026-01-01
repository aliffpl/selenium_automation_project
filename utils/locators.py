"""Locator helpers that provide `By` constants even if Selenium isn't installed."""
import importlib

def _get_selenium_by():
    try:
        mod = importlib.import_module('selenium.webdriver.common.by')
        return mod.By
    except Exception:
        class ByFallback:
            ID = 'id'
            XPATH = 'xpath'
            TAG_NAME = 'tag name'
            CSS_SELECTOR = 'css selector'
            NAME = 'name'
        return ByFallback

By = _get_selenium_by()
