from config import EXPLICIT_WAIT

try:
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    from selenium.common.exceptions import TimeoutException
    HAS_SELENIUM = True
except Exception:
    HAS_SELENIUM = False


def wait_for_element_visible(driver, by, locator, timeout: int = EXPLICIT_WAIT):
    if HAS_SELENIUM and not getattr(driver, 'is_fake', False):
        try:
            return WebDriverWait(driver, timeout).until(EC.visibility_of_element_located((by, locator)))
        except TimeoutException:
            return None
    try:
        return driver.find_element(by, locator)
    except Exception:
        return None


def wait_for_element_clickable(driver, by, locator, timeout: int = EXPLICIT_WAIT):
    if HAS_SELENIUM and not getattr(driver, 'is_fake', False):
        try:
            return WebDriverWait(driver, timeout).until(EC.element_to_be_clickable((by, locator)))
        except TimeoutException:
            return None
    try:
        return driver.find_element(by, locator)
    except Exception:
        return None


def wait_for_url_contains(driver, text: str, timeout: int = EXPLICIT_WAIT):
    if HAS_SELENIUM and not getattr(driver, 'is_fake', False):
        try:
            return WebDriverWait(driver, timeout).until(EC.url_contains(text))
        except TimeoutException:
            return False
    return text in getattr(driver, 'current_url', '')
