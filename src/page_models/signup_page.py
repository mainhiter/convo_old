from base_app import BasePage
from selenium.webdriver.common.by import By


class SignupPageLocators:
    SKIP_FOR_NOW_BUTTON = (By.XPATH, '//XCUIElementTypeButton[@name="Skip for now"]')
    FIRST_NAME_FIELD = (By.XPATH, '//XCUIElementTypeApplication[@name="Convo debug"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther[3]/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeScrollView/XCUIElementTypeOther[1]/XCUIElementTypeOther[2]/XCUIElementTypeOther[1]/XCUIElementTypeTextField')
    LAST_NAME_FIELD = (By.XPATH, '//XCUIElementTypeApplication[@name="Convo debug"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther[3]/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeScrollView/XCUIElementTypeOther[1]/XCUIElementTypeOther[2]/XCUIElementTypeOther[2]/XCUIElementTypeTextField')
    NEXT_BUTTON_1 = (By.XPATH, '//XCUIElementTypeButton[@name="Next"]')
    NEXT_BUTTON_2 = (By.XPATH, '//XCUIElementTypeApplication[@name="Convo debug"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther[3]/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeScrollView/XCUIElementTypeOther[1]/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeTextField')
    USERNAME_FIELD = (By.XPATH, '//XCUIElementTypeApplication[@name="Convo debug"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther[3]/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeScrollView/XCUIElementTypeOther[1]/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeTextField')
    DESCRIBE_FIELD = (By.XPATH, '//XCUIElementTypeApplication[@name="Convo debug"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther[3]/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeScrollView/XCUIElementTypeOther[1]/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeTextView')
    NEXT_BUTTON_3 = (By.XPATH, '//XCUIElementTypeButton[@name="Next"]')
    ARTS = (By.XPATH, '(//XCUIElementTypeStaticText[@name="Arts"])[1]')
    NEXT_BUTTON_4 = (By.XPATH, '//XCUIElementTypeButton[@name="Next"]')
    SKIP_FOR_NOW_BUTTON2 = (By.XPATH, '//XCUIElementTypeStaticText[@name="Skip for now"]')
    LETS_GO_BUTTON = (By.XPATH, '//XCUIElementTypeButton[@name="Let’s go!"]')




class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def click_navigation_bar_profile(self):
        return self.find_element(LoginPageLocators.NAVIGATION_BAR_PROFILE).click()