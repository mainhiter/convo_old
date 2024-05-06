from base_app import BasePage
from selenium.webdriver.common.by import By


class Locators:
    SEARCH_FIELD = (By.XPATH, '//XCUIElementTypeApplication[@name="Convo debug"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[1]/XCUIElementTypeOther/XCUIElementTypeTextField')
    NAVIGATION_BAR_SEARCH = (By.XPATH, '(//XCUIElementTypeButton[@name="Button"])[2]')
    TOP_TAB_BUTTON = (By.XPATH, '//XCUIElementTypeButton[@name="Top"]')
    CONVOS_TAB_BUTTON = (By.XPATH, '//XCUIElementTypeButton[@name="Convos"]')
    THOUGHTS_TAB_BUTTON = (By.XPATH, '//XCUIElementTypeButton[@name="Thoughts"]')
    PODS_TAB_BUTTON = (By.XPATH, '//XCUIElementTypeButton[@name="Pods"]')
    PEOPLE_TAB_BUTTON = (By.XPATH, '//XCUIElementTypeButton[@name="People"]')
    RESULT_SEARCH = (By.XPATH, '//XCUIElementTypeApplication[@name="Convo debug"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeCollectionView')
    SEE_ALL_CONVOS = (By.XPATH, '//XCUIElementTypeApplication[@name="Convo debug"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeCollectionView/XCUIElementTypeCell[1]/XCUIElementTypeOther/XCUIElementTypeButton')
    SEE_ALL_PEOPLE = (By.XPATH, '//XCUIElementTypeApplication[@name="Convo debug"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeCollectionView/XCUIElementTypeCell[3]/XCUIElementTypeOther/XCUIElementTypeButton')
    SEE_ALL_THOUGHTS = (By.XPATH, '//XCUIElementTypeApplication[@name="Convo debug"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeCollectionView/XCUIElementTypeCell[5]/XCUIElementTypeOther/XCUIElementTypeButton')
    SEE_ALL_PODS = (By.XPATH, '//XCUIElementTypeApplication[@name="Convo debug"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeCollectionView/XCUIElementTypeCell[6]/XCUIElementTypeOther/XCUIElementTypeButton')
    SEARCH_RESULT_PEOPLE = '//XCUIElementTypeStaticText[@name="{}"]'
    SEARCH_RESULT_PODS = '//XCUIElementTypeStaticText[@name="{}"]'
    SEARCH_RESULT_CONVOS = '//XCUIElementTypeStaticText[@name="{}"]'


class SearchPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def click_navigation_bar_search(self):
        return self.find_element(Locators.NAVIGATION_BAR_SEARCH).click()

    def click_search_field(self):
        return self.find_element(Locators.SEARCH_FIELD).click()

    def click_top_tab_button(self):
        return self.find_element(Locators.TOP_TAB_BUTTON).click()

    def click_convos_tab_button(self):
        return self.find_element(Locators.CONVOS_TAB_BUTTON).click()

    def click_thoughts_tab_button(self):
        return self.find_element(Locators.THOUGHTS_TAB_BUTTON).click()

    def click_pods_tab_button(self):
        return self.find_element(Locators.PODS_TAB_BUTTON).click()

    def click_people_tab_button(self):
        return self.find_element(Locators.PEOPLE_TAB_BUTTON).click()

    def fill_search(self, string):
        return self.find_element(Locators.SEARCH_FIELD).send_keys(string)

    def result_search(self, string):
        return self.find_element(Locators.RESULT_SEARCH).click()

    def click_search_result_people(self, name):
        return self.find_element((By.XPATH, Locators.SEARCH_RESULT_PEOPLE.format(name))).click()

    def click_search_result_convos(self, name):
        return self.find_element((By.XPATH, Locators.SEARCH_RESULT_CONVOS.format(name))).click()

    def click_search_result_pods(self, name):
        return self.find_element((By.XPATH, Locators.SEARCH_RESULT_PODS.format(name))).click()
