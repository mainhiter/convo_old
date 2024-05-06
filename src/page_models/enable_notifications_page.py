from base_app import BasePage
from selenium.webdriver.common.by import By


class Locators:
    SKIP_FOR_NOW_BUTTON = (By.XPATH, '//XCUIElementTypeButton[@name="Skip for now"]')


class EnableNotificationsPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def click_skip_for_now(self):
        return self.find_element(Locators.SKIP_FOR_NOW_BUTTON).click()

