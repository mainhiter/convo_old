from time import sleep

from page_models.navigation_bar import NavigationBar
from page_models.profile_page import ProfilePage
from utills.action_utills import sign_up_following, create_replay


def test_create_replay(appium):
    sign_up_following(appium)
    replay = create_replay(appium)
    profile = ProfilePage(appium)
    profile.click_thoughts_button_profile()
    assert replay['description'] == profile.get_last_thought()
