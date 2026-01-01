from utils.locators import By
from utils.waits import wait_for_element_visible

class LinksPage:
    URL = "/links"
    SIMPLE_LINK = (By.ID, "simpleLink")
    BAD_LINK = (By.ID, "badRequest")

    def __init__(self, driver, base_url):
        self.driver = driver
        self.base_url = base_url

    def open(self):
        self.driver.get(self.base_url + self.URL)

    def click_simple_link(self):
        el = wait_for_element_visible(self.driver, *self.SIMPLE_LINK)
        if el:
            el.click()

    def get_simple_link_href(self):
        el = wait_for_element_visible(self.driver, *self.SIMPLE_LINK)
        return el.get_attribute('href') if el else None
