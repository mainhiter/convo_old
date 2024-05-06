from base_app import BasePage
from selenium.webdriver.common.by import By

class Locators:
    LIKE_BUTTON = (By.XPATH, '//XCUIElementTypeButton[@name="like icon"]')
    REPLY_BUTTON = (By.XPATH, '//XCUIElementTypeButton[@name="reply icon"]')


class FullScreenPlayerPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def click_like_button(self):
        return self.find_element(Locators.LIKE_BUTTON).click()

    def click_reply_button(self):
        return self.find_element(Locators.REPLY_BUTTON).click()

    def click_back_button(self):
        return self.actions.tap(x=34, y=74).perform()


