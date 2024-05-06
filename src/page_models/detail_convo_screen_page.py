from base_app import BasePage
from selenium.webdriver.common.by import By


class Locators:
    AVATAR_PLAY_BUTTON = (By.XPATH, '//XCUIElementTypeApplication[@name="Convo debug"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeTable/XCUIElementTypeCell[1]/XCUIElementTypeButton[2]')


class DetailConvoScreenPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def click_play_convo(self):
        return self.find_element(Locators.AVATAR_PLAY_BUTTON).click()

    def click_back_button(self):
        return self.actions.tap(x=35, y=74).perform()
    # нет кнопки, чтобы по ней тапнуть