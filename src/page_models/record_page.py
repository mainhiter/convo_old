from base_app import BasePage
from selenium.webdriver.common.by import By


class Locators:
    START_RECORD_BUTTON = (By.XPATH, '//XCUIElementTypeButton[@name="record"]')
    NEXT_BUTTON = (By.XPATH, '//XCUIElementTypeButton[@name="Next"]')
    CLOSE_BUTTON = (By.XPATH, '//XCUIElementTypeButton[@name="close"]')
    STOP_RECORD_BUTTON = (By.XPATH, '//XCUIElementTypeButton[@name="record square"]')


class RecordPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def click_start_record_button(self):
        return self.find_element(Locators.START_RECORD_BUTTON).click()

    def click_next_button(self):
        return self.find_element(Locators.NEXT_BUTTON).click()

    def click_close_button(self):
        return self.find_element(Locators.CLOSE_BUTTON).click()

    def click_stop_record(self):
        return self.find_element(Locators.STOP_RECORD_BUTTON).click()
