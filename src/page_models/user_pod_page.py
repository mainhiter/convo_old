from base_app import BasePage
from selenium.webdriver.common.by import By


class Locators:
    FOLLOW_BUTTON = (By.XPATH, '//XCUIElementTypeButton[@name="Follow"]')
    UNFOLLOW_BUTTON = (By.XPATH, '//XCUIElementTypeButton[@name="Unfollow"]')
    CONVOS = '//XCUIElementTypeApplication[@name="Convo debug"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeTable/XCUIElementTypeCell'


class UserPodPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def click_follow_button(self):
        return self.find_element(Locators.FOLLOW_BUTTON).click()

    def click_unfollow_button(self):
        return self.find_element(Locators.UNFOLLOW_BUTTON).click()

    def get_convos_names(self):
        result = []
        convos = self.find_elements((By.XPATH, Locators.CONVOS))
        for convo_number in range(4, len(convos) + 1): # первые три элемента - не конво
            convo_name = self.find_element((By.XPATH, Locators.CONVOS + '[' + str(convo_number) + ']/XCUIElementTypeStaticText[5]'))
            result.append(convo_name.get_attribute('label'))
        return result