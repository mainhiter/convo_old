from base_app import BasePage
from selenium.webdriver.common.by import By


class HomePageLocators:
    FOR_YOU_BUTTON = (By.XPATH, '//XCUIElementTypeButton[@name="For you"]')
    FOLLOWING_BUTTON = (By.XPATH, '//XCUIElementTypeButton[@name="Following"]')
    RECORD_BUTTON = (By.XPATH,  '//XCUIElementTypeButton[@name="camera"]')
    NAVIGATION_BAR_HOME = (By.XPATH, '(//XCUIElementTypeButton[@name="Button"])[1]')


class HomePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def click_for_you_button(self):
        return self.find_element(HomePageLocators.FOR_YOU_BUTTON).click()

    def click_following_button(self):
        return self.find_element(HomePageLocators.FOLLOWING_BUTTON).click()

    def click_record_button(self):
        return self.find_element(HomePageLocators.RECORD_BUTTON).click()

    def click_navigation_bar_home(self):
        return self.find_element(HomePageLocators.NAVIGATION_BAR_HOME).click()

