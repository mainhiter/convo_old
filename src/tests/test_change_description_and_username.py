from page_models.profile_page import ProfilePage
from page_models.profile_settings_page import ProfileSettingsPage
from utills.action_utills import sign_up_following
from utills.random_utils import generate_random_first_name, generate_random_last_name, generate_random_username, \
    generate_random_description
from time import sleep


def test_change_description_and_username(appium):
    user = sign_up_following(appium)
    profile = ProfilePage(appium)
    settings = ProfileSettingsPage(appium)
    sleep(5)
    profile.click_settings_button_profile()
    settings.click_username()
    settings.clear_username_field()
    username = generate_random_username()
    settings.fill_username_field(username)
    settings.click_update_button()
    settings.click_bio()
    settings.clear_bio_field()
    bio = generate_random_description()
    settings.fill_bio_field(bio)
    settings.click_update_button()
    sleep(2)
    settings.click_back_button()
    assert "@" + user['username'] != profile.get_username()
    assert user['description'] != profile.get_description()