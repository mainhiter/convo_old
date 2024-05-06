from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import  *
from selenium.webdriver.common.by import By
from appium.webdriver.common.appiumby import AppiumBy
from selenium import webdriver
from appium.webdriver.common.touch_action import TouchAction
import requests
import time


class BasePage:
    def __init__(self, driver):
        self.driver = webdriver.Remote = driver
        self.actions = TouchAction(driver)

    def find_element(self, locator):
        return WebDriverWait(
            self.driver,
            timeout=10,
            poll_frequency=1,
            ignored_exceptions=[StaleElementReferenceException, TimeoutException],
        ).until(
            EC.presence_of_element_located(locator),
            message=f"Can't find element by locator {locator}",
        )

    def find_elements(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(
            EC.presence_of_all_elements_located(locator),
            message=f"Can't find element by locator {locator}",
        )

    def remove_keyboard(self):
        return self.driver.hide_keyboard()

    def wait(self, s):
        return time.sleep(s)
