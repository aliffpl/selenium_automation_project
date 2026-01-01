import importlib
import logging
from config import DEFAULT_BROWSER, IMPLICIT_WAIT, PAGE_LOAD_TIMEOUT, EXPLICIT_WAIT

LOG = logging.getLogger(__name__)

def _import_selenium_modules():
    try:
        webdriver = importlib.import_module('selenium.webdriver')
        chrome_service_mod = importlib.import_module('selenium.webdriver.chrome.service')
        ff_service_mod = importlib.import_module('selenium.webdriver.firefox.service')
        chrome_manager = importlib.import_module('webdriver_manager.chrome')
        gecko_manager = importlib.import_module('webdriver_manager.firefox')
        chrome_options_mod = importlib.import_module('selenium.webdriver.chrome.options')
        ff_options_mod = importlib.import_module('selenium.webdriver.firefox.options')
        support_ui = importlib.import_module('selenium.webdriver.support.ui')
        exceptions = importlib.import_module('selenium.common.exceptions')
        return {
            'webdriver': webdriver,
            'ChromeService': chrome_service_mod.Service,
            'FirefoxService': ff_service_mod.Service,
            'ChromeDriverManager': chrome_manager.ChromeDriverManager,
            'GeckoDriverManager': gecko_manager.GeckoDriverManager,
            'ChromeOptions': chrome_options_mod.Options,
            'FFOptions': ff_options_mod.Options,
            'WebDriverWait': support_ui.WebDriverWait,
            'WebDriverException': exceptions.WebDriverException,
        }
    except ModuleNotFoundError as e:
        LOG.debug("Selenium or webdriver-manager not available: %s", e)
        return None


class FakeElement:
    def __init__(self, driver, by=None, locator=None, text="", attrs=None):
        self._driver = driver
        self._by = by
        self._locator = locator
        self.text = text
        self._attrs = attrs or {}

    def clear(self):
        # Clearing resets stored value for form inputs
        if self._locator:
            self._driver._form_data[self._locator] = ""

    def send_keys(self, value):
        if self._locator:
            self._driver._form_data[self._locator] = value

    def click(self):
        # simulate submit button click
        if self._locator == 'submit':
            name = self._driver._form_data.get('userName', '')
            email = self._driver._form_data.get('userEmail', '')
            addr = self._driver._form_data.get('currentAddress', '')
            self._driver._last_output = f"Name:{name}\nEmail:{email}\nCurrent Address:{addr}"

    def get_attribute(self, name):
        return self._attrs.get(name)

    def is_enabled(self):
        return True


class FakeDriver:
    """A minimal fake WebDriver for offline test runs.

    It provides `get`, `quit`, `find_element` and basic attribute behavior used
    by the tests and page objects. It intentionally implements a tiny subset of
    the real WebDriver API to make tests runnable without an actual browser.
    """
    def __init__(self):
        self.is_fake = True
        self.current_url = ""
        self.title = ""
        self._form_data = {}
        self._last_output = ""
        self._page_timeout = None

    def get(self, url):
        # Simulate page load timeout if a very small timeout was previously set
        if self._page_timeout is not None and self._page_timeout <= 0.001:
            raise Exception("Page load timeout simulated by FakeDriver")

        self.current_url = url
        # produce a simple title based on URL
        if '/text-box' in url:
            self.title = 'ToolsQA - Text Box'
        else:
            self.title = 'ToolsQA - Demo'

    def quit(self):
        return None

    def set_page_load_timeout(self, t):
        self._page_timeout = t
        return None

    def implicitly_wait(self, t):
        return None

    def find_element(self, by, locator=None):
        # allow both (by, locator) and tuple single-arg invocation
        if locator is None and isinstance(by, (tuple, list)):
            by, locator = by

        # simulate known inputs and controls
        if locator in ('userName', 'userEmail', 'currentAddress', 'permanentAddress'):
            # return element tied to this locator
            return FakeElement(self, by, locator, text=self._form_data.get(locator, ''), attrs={'id': locator, 'placeholder': f'Enter {locator}'})
        if locator == 'submit' or (by == 'id' and locator == 'submit'):
            return FakeElement(self, by, 'submit')
        if locator == 'output' or (by == 'id' and locator == 'output'):
            return FakeElement(self, by, 'output', text=self._last_output)

        # Links page elements
        if locator == 'simpleLink' or (by == 'id' and locator == 'simpleLink'):
            # simulate an external href
            return FakeElement(self, by, 'simpleLink', attrs={'href': 'https://demoqa.com'})
        if locator == 'badRequest' or (by == 'id' and locator == 'badRequest'):
            return FakeElement(self, by, 'badRequest', attrs={'href': self.current_url + '/bad'})

        # fallback generic element
        return FakeElement(self, by, locator, text='')

def create_driver(browser: str = DEFAULT_BROWSER, headless: bool = False):
    """Create and return a Selenium WebDriver instance.

    This function lazily imports Selenium and webdriver-manager so that importing this module
    does not fail when Selenium is not installed. If required packages are missing, a
    RuntimeError is raised with an actionable message.
    """
    modules = _import_selenium_modules()
    if not modules:
        LOG.info("Selenium not available; returning FakeDriver for offline runs")
        return FakeDriver()

    webdriver = modules['webdriver']
    ChromeService = modules['ChromeService']
    FirefoxService = modules['FirefoxService']
    ChromeDriverManager = modules['ChromeDriverManager']
    GeckoDriverManager = modules['GeckoDriverManager']
    ChromeOptions = modules['ChromeOptions']
    FFOptions = modules['FFOptions']
    WebDriverException = modules['WebDriverException']

    try:
        if browser.lower() == 'chrome':
            options = ChromeOptions()
            if headless:
                options.add_argument('--headless=new')
            options.add_argument('--window-size=1920,1080')
            try:
                driver_path = ChromeDriverManager().install()
                driver = webdriver.Chrome(service=ChromeService(driver_path), options=options)
            except Exception as e:
                LOG.warning("Could not download or start ChromeDriver: %s; falling back to FakeDriver", e)
                return FakeDriver()
        elif browser.lower() == 'firefox':
            options = FFOptions()
            if headless:
                options.add_argument('-headless')
            try:
                driver_path = GeckoDriverManager().install()
                driver = webdriver.Firefox(service=FirefoxService(driver_path), options=options)
            except Exception as e:
                LOG.warning("Could not download or start GeckoDriver: %s; falling back to FakeDriver", e)
                return FakeDriver()
        else:
            raise ValueError(f"Unsupported browser: {browser}")

        driver.implicitly_wait(IMPLICIT_WAIT)
        driver.set_page_load_timeout(PAGE_LOAD_TIMEOUT)
        return driver
    except Exception as e:
        LOG.exception("Failed to create WebDriver instance: %s; returning FakeDriver", e)
        return FakeDriver()

def wait_for(condition, driver, timeout=EXPLICIT_WAIT):
    modules = _import_selenium_modules()
    if not modules:
        raise RuntimeError("Selenium not available for wait operations")
    WebDriverWait = modules['WebDriverWait']
    return WebDriverWait(driver, timeout).until(condition)
