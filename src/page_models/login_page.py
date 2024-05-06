from base_app import BasePage
from selenium.webdriver.common.by import By


class LoginPageLocators:
    NAVIGATION_BAR_PROFILE = (By.XPATH, '(//XCUIElementTypeButton[@name="Button"])[4]')
    LOGIN_BUTTON = (By.XPATH, '//XCUIElementTypeStaticText[@name="Log in or sign up"]')
    SIGN_UP_EMAIL = (By.XPATH, '//XCUIElementTypeStaticText[@name="Sign up with email"]')
    EMAIL_FIELD = (By.XPATH, '//XCUIElementTypeApplication[@name="Convo debug"]/XCUIElementTypeWindow/XCUIElementTypeOther[3]/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeScrollView/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeTextField')
    SEND_CODE_BUTTON = (By.XPATH, '//XCUIElementTypeStaticText[@name="Send code"]')
    CODE_INPUT_FIELD = (By.XPATH, '//XCUIElementTypeApplication[@name="Convo debug"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther[3]/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[3]')

class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def click_navigation_bar_profile(self):
        return self.find_element(LoginPageLocators.NAVIGATION_BAR_PROFILE).click()

    def click_login_button(self):
        return self.find_element(LoginPageLocators.LOGIN_BUTTON).click()

    def click_signup_email(self):
        return self.find_element(LoginPageLocators.SIGN_UP_EMAIL).click()

    def fill_email(self, string):
        return self.find_element(LoginPageLocators.EMAIL_FIELD).send_keys(string)

    def click_send_code(self):
        return self.find_element(LoginPageLocators.SEND_CODE_BUTTON).click()

    def fill_code(self, string):
        return self.find_element(LoginPageLocators.CODE_INPUT_FIELD).send_keys(string)
