from base_app import BasePage
from selenium.webdriver.common.by import By


class ProfilePageLocators:
    NAVIGATION_BAR_PROFILE = (By.XPATH, '(//XCUIElementTypeButton[@name="Button"])[4]')
    LOGIN_OR_SIGNUP_PROFILE = (By.XPATH, '//XCUIElementTypeButton[@name="Log in or sign up"]')
    EDIT_BUTTON_PROFILE = (By.XPATH, '//XCUIElementTypeButton[@name="Edit profile"]')
    ADD_BUTTON_PROFILE = (By.XPATH, '//XCUIElementTypeButton[@name="add"]')
    SETTINGS_BUTTON_PROFILE = (By.XPATH, '//XCUIElementTypeButton[@name="settings icon"]')
    FOLLOWERS_BUTTON_PROFILE = (By.XPATH, '//XCUIElementTypeButton[@name="Followers"]')
    FOLLOWING_BUTTON_PROFILE = (By.XPATH, '//XCUIElementTypeButton[@name="Following"]')
    CONVOS_BUTTON_PROFILE = (By.XPATH, '//XCUIElementTypeButton[@name="Convos"]')
    THOUGHTS_BUTTON_PROFILE = (By.XPATH, '//XCUIElementTypeButton[@name="Thoughts"]')
    PODS_BUTTON_PROFILE = (By.XPATH, '//XCUIElementTypeButton[@name="Pods"]')
    NEWCONVO_BUTTON_PROFILE = (By.XPATH, '//XCUIElementTypeButton[@name="Start a new convo"]')
    NEWPOD_BUTTON_PROFILE = (By.XPATH, '//XCUIElementTypeButton[@name="Start a new pod"]')
    NAME_TEXT = (By.XPATH, '//XCUIElementTypeApplication[@name="Convo debug"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeStaticText')
    USERNAME_TEXT = (By.XPATH, '//XCUIElementTypeApplication[@name="Convo debug"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeCollectionView/XCUIElementTypeCell[1]/XCUIElementTypeOther/XCUIElementTypeStaticText[1]')
    DESCRIPTION_TEXT = (By.XPATH, '//XCUIElementTypeApplication[@name="Convo debug"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeCollectionView/XCUIElementTypeCell[1]/XCUIElementTypeOther/XCUIElementTypeStaticText[2]')
    CONVO_ITEMS = (By.XPATH, '//XCUIElementTypeApplication[@name="Convo debug"]/XCUIElementTypeWindow/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeCollectionView/XCUIElementTypeCell[4]/XCUIElementTypeOther/XCUIElementTypeStaticText[3]')
    THOUGHTS_ITEMS = (By.XPATH, '//XCUIElementTypeApplication[@name="Convo debug"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeCollectionView/XCUIElementTypeCell[4]/XCUIElementTypeOther/XCUIElementTypeStaticText[3]')


class ProfilePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def click_login_or_signup_profile(self):
        return self.find_element(ProfilePageLocators.LOGIN_OR_SIGNUP_PROFILE).click()

    def click_edit_button_profile(self):
        return self.find_element(ProfilePageLocators.EDIT_BUTTON_PROFILE).click()

    def click_add_button_profile(self):
        return self.find_element(ProfilePageLocators.ADD_BUTTON_PROFILE).click()

    def click_settings_button_profile(self):
        return self.find_element(ProfilePageLocators.SETTINGS_BUTTON_PROFILE).click()

    def click_followers_button_profile(self):
        return self.find_element(ProfilePageLocators.FOLLOWERS_BUTTON_PROFILE).click()

    def click_following_button_profile(self):
        return self.find_element(ProfilePageLocators.FOLLOWING_BUTTON_PROFILE).click()

    def click_convos_button_profile(self):
        return self.find_element(ProfilePageLocators.CONVOS_BUTTON_PROFILE).click()

    def click_thoughts_button_profile(self):
        return self.find_element(ProfilePageLocators.THOUGHTS_BUTTON_PROFILE).click()

    def click_pods_button_profile(self):
        return self.find_element(ProfilePageLocators.PODS_BUTTON_PROFILE).click()

    def click_newconvo_button_profile(self):
        return self.find_element(ProfilePageLocators.NEWCONVO_BUTTON_PROFILE).click()

    def click_newpod_button_profile(self):
        return self.find_element(ProfilePageLocators.NEWPOD_BUTTON_PROFILE).click()

    def get_name(self):
        return self.find_element(ProfilePageLocators.NAME_TEXT).get_attribute("label")

    def get_username(self):
        return self.find_element(ProfilePageLocators.USERNAME_TEXT).get_attribute("label")

    def get_description(self):
        return self.find_element(ProfilePageLocators.DESCRIPTION_TEXT).get_attribute("label")

    def get_last_convo(self):
        return self.find_element(ProfilePageLocators.CONVO_ITEMS).get_attribute("label")

    def click_last_convo(self):
        return self.find_element(ProfilePageLocators.CONVO_ITEMS).click()

    def get_last_thought(self):
        return self.find_element(ProfilePageLocators.THOUGHTS_ITEMS).get_attribute("label")