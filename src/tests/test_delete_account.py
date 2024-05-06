from page_models.home_page import HomePage
from time import sleep
from page_models.navigation_bar import NavigationBar
from page_models.profile_page import ProfilePage
from page_models.profile_settings_page import ProfileSettingsPage
from utills.action_utills import sign_up_following


def test_delete_account(appium):
    sign_up_following(appium)
    navigation_bar = NavigationBar(appium)
    profile = ProfilePage(appium)
    settings = ProfileSettingsPage(appium)
    home = HomePage(appium)
    navigation_bar.click_navigation_bar_profile()
    profile.click_settings_button_profile()
    settings.click_delete_button()
    settings.click_delete_confirmation_button()
    sleep(3)
    home.click_following_button()
    # нет ассёрта потому что после удаления юзер попадает на home и если он смог там перейти на другую вкладку home - значит всё хорошо








