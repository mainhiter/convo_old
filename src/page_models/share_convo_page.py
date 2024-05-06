from base_app import BasePage
from selenium.webdriver.common.by import By


class Locators:
    TITLE_FIELD = (By.XPATH, '//XCUIElementTypeOther[@name="Title"]/XCUIElementTypeTextField[1]')
    DESCRIPTION_FIELD = (By.XPATH, '//XCUIElementTypeApplication[@name="Convo debug"]/XCUIElementTypeWindow/XCUIElementTypeOther[3]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeTable/XCUIElementTypeTextField[2]')
    SHARE_BUTTON = (By.XPATH, '//XCUIElementTypeButton[@name="Share"]')
    BACK_BUTTON = (By.XPATH, '//XCUIElementTypeButton[@name="back icon"]')


class ShareConvoPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def click_title_field(self):
        return self.find_element(Locators.TITLE_FIELD).click()

    def click_description_field(self):
        return self.find_element(Locators.DESCRIPTION_FIELD).click()

    def click_share_button(self):
        return self.find_element(Locators.SHARE_BUTTON).click()

    def fill_title_field(self, string):
        return self.find_element(Locators.TITLE_FIELD).send_keys(string)

    def click_back_button(self):
        return self.find_element(Locators.BACK_BUTTON).click()
