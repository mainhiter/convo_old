from base_app import BasePage
from selenium.webdriver.common.by import By


class Locators:
    LOGOUT_BUTTON = (By.XPATH, '//XCUIElementTypeApplication[@name="Convo debug"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeTable/XCUIElementTypeCell[11]')
    LOGOUT_CONFIRMATION_BUTTON = (By.XPATH, '//XCUIElementTypeApplication[@name="Convo debug"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther[3]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeTable/XCUIElementTypeCell[1]')
    DELETE_BUTTON = (By.XPATH, '//XCUIElementTypeApplication[@name="Convo debug"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeTable/XCUIElementTypeCell[13]')
    DELETE_CONFIRMATION_BUTTON = (By.XPATH, '//XCUIElementTypeApplication[@name="Convo debug"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther[3]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeTable/XCUIElementTypeCell[1]')
    NAME_FIELD = (By.XPATH, '//XCUIElementTypeApplication[@name="Convo debug"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeTable/XCUIElementTypeCell[2]')
    LAST_NAME_FIELD = (By.XPATH, '//XCUIElementTypeApplication[@name="Convo debug"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeTable/XCUIElementTypeCell[2]/XCUIElementTypeTextField')
    UPDATE_BUTTON = (By.XPATH, '//XCUIElementTypeButton[@name="Update"]')
    BACK_BUTTON = (By.XPATH, '//XCUIElementTypeButton[@name="back icon"]')
    FIRST_NAME_FIELD = (By.XPATH, '//XCUIElementTypeApplication[@name="Convo debug"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeTable/XCUIElementTypeCell[1]/XCUIElementTypeTextField')
    EDIT_NAME_TEXT = (By.XPATH, '//XCUIElementTypeStaticText[@name="Edit name"]')
    FIRST_NAME_TEXT = (By.XPATH, '//XCUIElementTypeApplication[@name="Convo debug"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeTable/XCUIElementTypeCell[1]/XCUIElementTypeTextField')
    LAST_NAME_TEXT = (By.XPATH, '//XCUIElementTypeApplication[@name="Convo debug"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeTable/XCUIElementTypeCell[2]/XCUIElementTypeTextField')
    USERNAME_BUTTON = (By.XPATH, '(//XCUIElementTypeButton[@name="chevron"])[2]')
    BIO_BUTTON = (By.XPATH, '(//XCUIElementTypeButton[@name="chevron"])[4]')
    USERNAME_FIELD = (By.XPATH, '//XCUIElementTypeApplication[@name="Convo debug"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeTable/XCUIElementTypeCell/XCUIElementTypeTextField')
    BIO_FIELD = (By.XPATH, '//XCUIElementTypeApplication[@name="Convo debug"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeTable/XCUIElementTypeCell/XCUIElementTypeTextView')


class ProfileSettingsPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def click_logout_button(self):
        return self.find_element(Locators.LOGOUT_BUTTON).click()

    def click_logout_confirmation_button(self):
        return self.find_element(Locators.LOGOUT_CONFIRMATION_BUTTON).click()

    def click_delete_button(self):
        return self.find_element(Locators.DELETE_BUTTON).click()

    def click_delete_confirmation_button(self):
        return self.find_element(Locators.DELETE_CONFIRMATION_BUTTON).click()

    def click_name_field(self):
        return self.find_element(Locators.NAME_FIELD).click()

    def click_last_name_field(self):
        return self.find_element(Locators.LAST_NAME_FIELD).click()

    def clear_last_name_field(self):
        return self.find_element(Locators.LAST_NAME_FIELD).clear()

    def clear_first_name_field(self):
        return self.find_element(Locators.FIRST_NAME_FIELD).clear()

    def click_update_button(self):
        return self.find_element(Locators.UPDATE_BUTTON).click()

    def click_back_button(self):
        return self.find_element(Locators.BACK_BUTTON).click()

    def fill_first_name_field(self, string):
        return self.find_element(Locators.FIRST_NAME_FIELD).send_keys(string)

    def fill_last_name_field(self, string):
        return self.find_element(Locators.LAST_NAME_FIELD).send_keys(string)

    def click_edit_name(self):
        return self.find_element(Locators.EDIT_NAME_TEXT).click()
    # эта хуйня, чтобы убрать системную подсказку в поле

    def get_first_name(self):
        return self.find_element(Locators.FIRST_NAME_TEXT).get_attribute("value")

    def get_last_name(self):
        return self.find_element(Locators.LAST_NAME_TEXT).get_attribute("value")

    def click_username(self):
        return self.find_element(Locators.USERNAME_BUTTON).click()

    def click_bio(self):
        return self.find_element(Locators.BIO_BUTTON).click()

    def clear_username_field(self):
        return self.find_element(Locators.USERNAME_FIELD).clear()

    def clear_bio_field(self):
        return self.find_element(Locators.BIO_FIELD).clear()

    def fill_username_field(self, string):
        return self.find_element(Locators.USERNAME_FIELD).send_keys(string)

    def fill_bio_field(self, string):
        return self.find_element(Locators.BIO_FIELD).send_keys(string)