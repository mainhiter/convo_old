from base_app import BasePage
from selenium.webdriver.common.by import By


class Locators:
    NAVIGATION_BAR_HOME = (By.XPATH, '(//XCUIElementTypeButton[@name="Button"])[1]')
    NAVIGATION_BAR_LIBRARY = (By.XPATH, '//XCUIElementTypeButton[@name="library active"]')
    NAVIGATION_BAR_SEARCH = (By.XPATH, '(//XCUIElementTypeButton[@name="Button"])[2]')
    NAVIGATION_BAR_ACTIVITY = (By.XPATH, '(//XCUIElementTypeButton[@name="Button"])[3]')
    NAVIGATION_BAR_PROFILE = (By.XPATH, '(//XCUIElementTypeButton[@name="Button"])[4]')


class NavigationBar(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def click_navigation_bar_profile(self):
        return self.find_element(Locators.NAVIGATION_BAR_PROFILE).click()

    def click_navigation_bar_home(self):
        return self.find_element(Locators.NAVIGATION_BAR_HOME).click()

    def click_navigation_bar_library(self):
        return self.find_element(Locators.NAVIGATION_BAR_LIBRARY).click()

    def click_navigation_bar_search(self):
        return self.find_element(Locators.NAVIGATION_BAR_SEARCH).click()

    def click_navigation_bar_activity(self):
        return self.find_element(Locators.NAVIGATION_BAR_ACTIVITY).click()