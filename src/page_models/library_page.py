from base_app import BasePage
from selenium.webdriver.common.by import By


class Locators:
    NAVIGATION_BAR_LIBRARY = (By.XPATH, '//XCUIElementTypeButton[@name="library active"]')
    PODS_YOU_FOLLOW_TAB = (By.XPATH, '//XCUIElementTypeButton[@name="Pods you follow"]')
    LATEST_CONVOS_TAB = (By.XPATH, '//XCUIElementTypeButton[@name="Latest Convos"]')
    HEADER_LIBRARY = (By.XPATH, '//XCUIElementTypeStaticText[@name="Library"]')
    CONVOS = '//XCUIElementTypeApplication[@name="Convo debug"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeScrollView/XCUIElementTypeOther/XCUIElementTypeCollectionView[2]/XCUIElementTypeCell'
    FIRST_POD = (By.XPATH, '//XCUIElementTypeApplication[@name="Convo debug"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeScrollView/XCUIElementTypeOther/XCUIElementTypeCollectionView[1]/XCUIElementTypeCell[1]/XCUIElementTypeOther/XCUIElementTypeStaticText[2]')

class LibraryPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def click_pods_you_follow_tab(self):
        return self.find_element(Locators.PODS_YOU_FOLLOW_TAB).click()

    def click_latest_convos_tab(self):
        return self.find_element(Locators.LATEST_CONVOS_TAB).click()

    def click_navigation_bar_library(self):
        return self.find_element(Locators.NAVIGATION_BAR_LIBRARY).click()

    def get_convos_names(self):
        result = []
        convos = self.find_elements((By.XPATH, Locators.CONVOS))
        for convo_number in range(1, len(convos) + 1):
            convo_name = self.find_element((By.XPATH, Locators.CONVOS + '[' + str(convo_number) + ']/XCUIElementTypeOther/XCUIElementTypeStaticText[3]'))
            result.append(convo_name.get_attribute('label'))
        return result

    def get_first_pod_name(self):
        return self.find_element(Locators.FIRST_POD).get_attribute('label')
