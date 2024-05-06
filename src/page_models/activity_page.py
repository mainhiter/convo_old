from base_app import BasePage
from selenium.webdriver.common.by import By


class ActivityPageLocators:
    NAVIGATION_BAR_ACTIVITY = (By.XPATH, '(//XCUIElementTypeButton[@name="Button"])[3]')
    ACTIVITY_HEADER = (By.XPATH, '//XCUIElementTypeStaticText[@name="Activity"]')
    ACTIVITIES = '//XCUIElementTypeApplication[@name="Convo debug"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeTable/XCUIElementTypeAny'


class ActivityPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def click_navigation_bar_activity(self):
        return self.find_element(ActivityPageLocators.NAVIGATION_BAR_ACTIVITY).click()

    def click_activity_header(self):
        return self.find_element(ActivityPageLocators.ACTIVITY_HEADER).click()

    def get_activities(self):
        result = []
        activities = self.find_elements((By.XPATH, ActivityPageLocators.ACTIVITIES))
        for activity_number in range(1, len(activities) + 1):
            activity_items = self.find_elements((By.XPATH, ActivityPageLocators.ACTIVITIES + '[' + str(activity_number) + ']/XCUIElementTypeStaticText'))
            activity_text = []
            for activity_item in activity_items:
                activity_text.append(activity_item.get_attribute('label'))
            result.append(' '.join(activity_text))
        return result
