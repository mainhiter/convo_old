from base_app import BasePage
from selenium.webdriver.common.by import By


class Locators:
    USERNAME_FILED = (By.XPATH, '//XCUIElementTypeApplication[@name="Convo debug"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther[3]/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeScrollView/XCUIElementTypeOther[1]/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeTextField')
    NEXT_BUTTON = (By.XPATH, '//XCUIElementTypeButton[@name="Next"]')


class PickUsernamePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def click_username_field(self):
        return self.find_element(Locators.USERNAME_FILED).click()

    def click_next_button(self):
        return self.find_element(Locators.NEXT_BUTTON).click()

    def fill_username_field(self, string):
        return self.find_element(Locators.USERNAME_FILED).send_keys(string)