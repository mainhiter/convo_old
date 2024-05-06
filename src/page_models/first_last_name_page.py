from base_app import BasePage
from selenium.webdriver.common.by import By


class Locators:
    FIRST_NAME_FIELD = (By.XPATH, '//XCUIElementTypeApplication[@name="Convo debug"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther[3]/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeScrollView/XCUIElementTypeOther[1]/XCUIElementTypeOther[2]/XCUIElementTypeOther[1]/XCUIElementTypeTextField')
    LAST_NAME_FIELD = (By.XPATH, '//XCUIElementTypeApplication[@name="Convo debug"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther[3]/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeScrollView/XCUIElementTypeOther[1]/XCUIElementTypeOther[2]/XCUIElementTypeOther[2]/XCUIElementTypeTextField')
    NEXT_BUTTON = (By.XPATH, '//XCUIElementTypeButton[@name="Next"]')


class FirstLastNamePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def click_first_name_field(self):
        return self.find_element(Locators.FIRST_NAME_FIELD).click()

    def click_last_name_field(self):
        return self.find_element(Locators.LAST_NAME_FIELD).click()

    def fill_first_name_field(self, string):
        return self.find_element(Locators.FIRST_NAME_FIELD).send_keys(string)

    def fill_last_name_field(self, string):
        return self.find_element(Locators.LAST_NAME_FIELD).send_keys(string)

    def click_next_button(self):
        return self.find_element(Locators.NEXT_BUTTON).click()