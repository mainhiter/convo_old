from time import sleep

from page_models.navigation_bar import NavigationBar
from page_models.profile_page import ProfilePage
from utills.action_utills import sign_up_following, create_convo_5min


def test_create_convo_5min(appium):
    sign_up_following(appium)
    convo = create_convo_5min(appium)
    profile_page = ProfilePage(appium)
    navigation_bar = NavigationBar(appium)
    navigation_bar.click_navigation_bar_profile()
    sleep(30)
    assert convo['title'] == profile_page.get_last_convo()
