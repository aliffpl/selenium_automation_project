from utils.locators import By
from utils.waits import wait_for_element_visible, wait_for_element_clickable

class TextBoxPage:
    URL = "/text-box"
    INPUT_FULL_NAME = (By.ID, "userName")
    INPUT_EMAIL = (By.ID, "userEmail")
    INPUT_CURRENT_ADDRESS = (By.ID, "currentAddress")
    INPUT_PERMANENT_ADDRESS = (By.ID, "permanentAddress")
    BUTTON_SUBMIT = (By.ID, "submit")
    OUTPUT = (By.ID, "output")

    def __init__(self, driver, base_url):
        self.driver = driver
        self.base_url = base_url

    def open(self):
        self.driver.get(self.base_url + self.URL)

    def fill_form(self, name, email, current_address, permanent_address=None):
        wait_for_element_visible(self.driver, *self.INPUT_FULL_NAME).clear()
        self.driver.find_element(*self.INPUT_FULL_NAME).send_keys(name)
        self.driver.find_element(*self.INPUT_EMAIL).send_keys(email)
        self.driver.find_element(*self.INPUT_CURRENT_ADDRESS).send_keys(current_address)
        if permanent_address:
            self.driver.find_element(*self.INPUT_PERMANENT_ADDRESS).send_keys(permanent_address)

    def submit(self):
        wait_for_element_clickable(self.driver, *self.BUTTON_SUBMIT).click()

    def get_output_text(self):
        out = wait_for_element_visible(self.driver, *self.OUTPUT)
        return out.text if out else ""
