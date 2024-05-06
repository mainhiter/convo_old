from page_models.activity_page import ActivityPage
from page_models.navigation_bar import NavigationBar
from page_models.user_profile_page import UserProfilePage
from utills.action_utills import sign_up_following, logout, find_user, login, create_convo, like


def test_like_convo(appium):
    user1 = sign_up_following(appium)
    convo = create_convo(appium)
    logout(appium)
    user2 = sign_up_following(appium)
    like(convo['title'], appium)
    logout(appium)
    login(user1['inbox'], appium)
    navigation_bar = NavigationBar(appium)
    navigation_bar.click_navigation_bar_activity()
    activity_page = ActivityPage(appium)
    assert user2['first_name'] + ' ' + user2['last_name'] + ' TODAY  liked to your thought' in activity_page.get_activities()

