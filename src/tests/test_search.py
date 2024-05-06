from page_models.search_page import SearchPage
from appium.webdriver.common.appiumby import AppiumBy



def test_search_people(appium):
    search = SearchPage(appium)
    search.click_navigation_bar_search()
    search.actions.tap(x=388, y=124).perform()
    search.click_search_field()
    search.fill_search('Kolya')
    search.wait(2)
    result = search.find_element((AppiumBy.ACCESSIBILITY_ID, 'Kolyanchik Destroyer'))
    assert 'Kolyanchik Destroyer' in result.text


def test_search_top(appium):
    search = SearchPage(appium)
    search.click_navigation_bar_search()
    search.click_search_field()
    search.fill_search('Kolya')
    search.wait(2)
    result = search.find_element((AppiumBy.ACCESSIBILITY_ID, 'Kolyanchik Destroyer'))
    assert 'Kolyanchik Destroyer' in result.text


def test_search_convos(appium):
    search = SearchPage(appium)
    search.click_navigation_bar_search()
    search.click_convos_tab_button()
    search.click_search_field()
    search.fill_search('300')
    search.wait(2)
    result = search.find_element((AppiumBy.ACCESSIBILITY_ID, 'Omg 300'))
    assert 'Omg 300' in result.text


def test_search_thoughts(appium):
    search = SearchPage(appium)
    search.click_navigation_bar_search()
    search.click_thoughts_tab_button()
    search.click_search_field()
    search.fill_search('do_not_delete')
    search.wait(2)
    result = search.find_element((AppiumBy.ACCESSIBILITY_ID, 'do_not_delete'))
    assert 'do_not_delete' in result.text


def test_search_pods(appium):
    search = SearchPage(appium)
    search.click_navigation_bar_search()
    search.click_pods_tab_button()
    search.click_search_field()
    search.fill_search('do_not_delete')
    search.wait(2)
    result = search.find_element((AppiumBy.ACCESSIBILITY_ID, 'do_not_delete'))
    assert 'do_not_delete' in result.text





