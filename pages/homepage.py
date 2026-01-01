from utils.locators import By
from utils.waits import wait_for_element_visible
from config import BASE_URL

class HomePage:
    URL = BASE_URL + "/"
    TITLE = "ToolsQA"
    # example element: Elements card
    ELEMENTS_CARD = (By.XPATH, "//div[contains(@class,'card-body')]/h5[text()='Elements']/..")

    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get(self.URL)

    def is_loaded(self):
        return self.driver.title.startswith(self.TITLE)

    def wait_for_elements_card(self):
        return wait_for_element_visible(self.driver, *self.ELEMENTS_CARD)
