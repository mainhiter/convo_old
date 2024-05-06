from base_app import BasePage
from selenium.webdriver.common.by import By


class Locators:
    DESCRIBE_FILED = (By.XPATH,'//XCUIElementTypeApplication[@name="Convo debug"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther[3]/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeScrollView/XCUIElementTypeOther[1]/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeTextView')
    NEXT_BUTTON = (By.XPATH, '//XCUIElementTypeButton[@name="Next"]')


class DescribeYourselfPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def click_describe_field(self):
        return self.find_element(Locators.DESCRIBE_FILED).click()

    def click_next_button(self):
        return self.find_element(Locators.NEXT_BUTTON).click()

    def fill_describe_field(self, string):
        return self.find_element(Locators.DESCRIBE_FILED).send_keys(string)