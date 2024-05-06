from base_app import BasePage
from selenium.webdriver.common.by import By


class Locators:
    ARTS_BUTTON = (By.XPATH,'(//XCUIElementTypeStaticText[@name="Arts"])[1]')
    NEXT_BUTTON = (By.XPATH, '//XCUIElementTypeButton[@name="Next"]')


class InterestsPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def click_arts(self):
        return self.find_element(Locators.ARTS_BUTTON).click()

    def click_next_button(self):
        return self.find_element(Locators.NEXT_BUTTON).click()