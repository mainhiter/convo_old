from page_models.search_page import SearchPage


def test_swipe(appium):
    search = SearchPage(appium)
    search.click_navigation_bar_search()
    search.actions.press(x=320, y=140).wait(600).move_to(x=160, y=140).release().perform()
    search.click_people_tab_button()