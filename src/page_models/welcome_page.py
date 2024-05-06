from base_app import BasePage
from selenium.webdriver.common.by import By


class Locators:
    LETS_GO_BUTTON = (By.XPATH, '//XCUIElementTypeButton[@name="Let’s go!"]')


class WelcomePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def click_letsgo(self):
        return self.find_element(Locators.LETS_GO_BUTTON).click()