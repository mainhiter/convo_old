from page_models.profile_page import ProfilePage
from utills.action_utills import sign_up_following


def test_sign_up_following(appium):
    user = sign_up_following(appium)
    profile_page = ProfilePage(appium)
    assert user['first_name'] + " " + user['last_name'] == profile_page.get_name()
    assert "@" + user['username'] == profile_page.get_username()
    assert user['description'] == profile_page.get_description()