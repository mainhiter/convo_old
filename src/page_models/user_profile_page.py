from base_app import BasePage
from selenium.webdriver.common.by import By


class Locators:
    FOLLOW_BUTTON = (By.XPATH, '//XCUIElementTypeButton[@name="Follow"]')


class UserProfilePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def click_follow_button(self):
        return self.find_element(Locators.FOLLOW_BUTTON).click()
