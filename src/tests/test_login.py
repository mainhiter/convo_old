from page_models.login_page import LoginPage
from page_models.profile_page import ProfilePageLocators, ProfilePage
from page_models.home_page import HomePage
from mail_client import get_code_from_email


def test_login_profile(appium):
    login = LoginPage(appium)
    login.click_navigation_bar_profile()
    login.click_login_button()
    login.click_signup_email()
    login.fill_email('a12d6c1b-f20b-43c6-941b-ede09b7c1b2f@mailslurp.com')
    login.click_send_code()
    code = get_code_from_email()
    login.fill_code(code)
    profile = ProfilePage(appium)
    edit_profile_text = profile.find_element(ProfilePageLocators.EDIT_BUTTON_PROFILE).text
    assert 'Edit profile' in edit_profile_text

def test_login_home(appium):
    home = HomePage(appium)
    home.click_following_button()
    login = LoginPage(appium)
    login.click_login_button()
    login.click_signup_email()
    login.fill_email('a12d6c1b-f20b-43c6-941b-ede09b7c1b2f@mailslurp.com')
    login.click_send_code()
    code = get_code_from_email()
    login.fill_code(code)


