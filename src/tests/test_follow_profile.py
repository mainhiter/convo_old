from page_models.activity_page import ActivityPage
from page_models.navigation_bar import NavigationBar
from page_models.user_profile_page import UserProfilePage
from utills.action_utills import sign_up_following, logout, find_user, login


def test_follow_profile(appium):
    user1 = sign_up_following(appium)
    logout(appium)
    user2 = sign_up_following(appium)
    find_user(user1['first_name'] + ' ' + user1['last_name'], appium)
    user_profile_page = UserProfilePage(appium)
    user_profile_page.click_follow_button()
    logout(appium)
    login(user1['inbox'], appium)
    navigation_bar = NavigationBar(appium)
    navigation_bar.click_navigation_bar_activity()
    activity_page = ActivityPage(appium)
    assert user2['first_name'] + ' ' + user2['last_name'] + ' TODAY followed you' in activity_page.get_activities()

