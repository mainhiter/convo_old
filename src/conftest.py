from appium import webdriver
import pytest


@pytest.fixture(scope="function")
def appium():
    desired_capabilities = {
        "platformName": "iOS",
        "appium:automationName": "XCUITest",
        "appium:deviceName": "iPhone 11",
        "appium:app": "/Users/doubletapp/Desktop/Convo debug.app",
        "appium:newCommandTimeout": "2000",
        "appium:autoAcceptAlerts": "true",
    }
    driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_capabilities)
    driver.implicitly_wait(10)
    return driver
