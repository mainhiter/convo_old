from base_app import BasePage
from selenium.webdriver.common.by import By


class Locators:
    PLUS_RECORD_BUTTON = (By.XPATH, '//XCUIElementTypeButton[@name="addMore"]')
    SHARE_BUTTON = (By.XPATH, '//XCUIElementTypeButton[@name="Share"]')
    DESCRIPTION_THOUGHT_FIELD = (By.XPATH, '//XCUIElementTypeApplication[@name="Convo debug"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther[4]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[3]/XCUIElementTypeTextField')
    DONE_KEYBOARD_BUTTON = (By.XPATH, '//XCUIElementTypeButton[@name="Done"]')

class ReviewConvoPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def click_plus_record_button(self):
        return self.find_element(Locators.PLUS_RECORD_BUTTON).click()

    def click_share_button(self):
        return self.find_element(Locators.SHARE_BUTTON).click()

    def click_description_field(self):
        return self.find_element(Locators.DESCRIPTION_THOUGHT_FIELD).click()

    def fill_description_field(self, string):
        return self.find_element(Locators.DESCRIPTION_THOUGHT_FIELD).send_keys(string)

    def clear_description_field(self):
        return self.find_element(Locators.DESCRIPTION_THOUGHT_FIELD).clear()

    def click_done_keyboard_button(self):
        return self.find_element(Locators.DONE_KEYBOARD_BUTTON).click()