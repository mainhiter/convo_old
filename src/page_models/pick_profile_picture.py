from base_app import BasePage
from selenium.webdriver.common.by import By


class Locators:
    SKIP_BUTTON = (By.XPATH,'//XCUIElementTypeButton[@name="Skip for now"]')


class PickProfilePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def click_skip(self):
        return self.find_element(Locators.SKIP_BUTTON).click()