from time import sleep

from page_models.describe_yourself_page import DescribeYourselfPage
from page_models.detail_convo_screen_page import DetailConvoScreenPage
from page_models.fullscreen_player_page import FullScreenPlayerPage
from page_models.interests_page import InterestsPage
from page_models.login_page import LoginPage
from page_models.home_page import HomePage
from page_models.enable_notifications_page import EnableNotificationsPage
from page_models.first_last_name_page import FirstLastNamePage
from mail_client import create_inbox, get_code_from_email2
from page_models.navigation_bar import NavigationBar
from page_models.pick_profile_picture import PickProfilePage
from page_models.pick_username_page import PickUsernamePage
from page_models.profile_page import ProfilePage
from page_models.profile_settings_page import ProfileSettingsPage
from page_models.record_page import RecordPage
from page_models.review_convo_page import ReviewConvoPage
from page_models.search_page import SearchPage
from page_models.share_convo_page import ShareConvoPage
from page_models.welcome_page import WelcomePage
from utills.random_utils import generate_random_first_name, generate_random_last_name, \
    generate_random_username, generate_random_description


def sign_up_following(appium):
    inbox = create_inbox()
    home_page = HomePage(appium)
    home_page.click_following_button()
    login = LoginPage(appium)
    login.click_login_button()
    login.click_signup_email()
    login.fill_email(inbox["email"])
    login.click_send_code()
    code = get_code_from_email2(inbox["id"])
    login.fill_code(code)
    enable_notifications_page = EnableNotificationsPage(appium)
    enable_notifications_page.click_skip_for_now()
    first_last_name_page = FirstLastNamePage(appium)
    first_last_name_page.click_first_name_field()
    first_name = generate_random_first_name()
    first_last_name_page.fill_first_name_field(first_name)
    first_last_name_page.click_last_name_field()
    last_name = generate_random_last_name()
    first_last_name_page.fill_last_name_field(last_name)
    first_last_name_page.click_next_button()
    username_page = PickUsernamePage(appium)
    username_page.click_username_field()
    username = generate_random_username()
    username_page.fill_username_field(username)
    username_page.click_next_button()
    describe_yourself = DescribeYourselfPage(appium)
    describe_yourself.click_describe_field()
    description = generate_random_description()
    describe_yourself.fill_describe_field(description)
    describe_yourself.click_next_button()
    interests_page = InterestsPage(appium)
    interests_page.click_arts()
    interests_page.click_next_button()
    pick_profile_page = PickProfilePage(appium)
    pick_profile_page.click_skip()
    welcome_page = WelcomePage(appium)
    welcome_page.click_letsgo()
    navigation_bar_profile = NavigationBar(appium)
    navigation_bar_profile.click_navigation_bar_profile()

    return {
        'username': username,
        'first_name': first_name,
        'last_name': last_name,
        'inbox': inbox,
        'description': description,
    }


def logout(appium):
    navigation_bar = NavigationBar(appium)
    navigation_bar.click_navigation_bar_profile()
    profile_page = ProfilePage(appium)
    profile_page.click_settings_button_profile()
    profile_settings_page = ProfileSettingsPage(appium)
    profile_settings_page.click_logout_button()
    profile_settings_page.click_logout_confirmation_button()


def find_user(name, appium):
    navigation_bar = NavigationBar(appium)
    navigation_bar.click_navigation_bar_search()
    search_page = SearchPage(appium)
    search_page.actions.tap(x=388, y=124).perform()
    search_page.click_search_field()
    search_page.fill_search(name)
    search_page.click_search_result_people(name)


def login(inbox, appium):
    navigation_bar = NavigationBar(appium)
    navigation_bar.click_navigation_bar_home()
    home = HomePage(appium)
    home.click_following_button()
    login_page = LoginPage(appium)
    login_page.click_login_button()
    login_page.click_signup_email()
    login_page.fill_email(inbox['email'])
    login_page.click_send_code()
    code = get_code_from_email2(inbox['id'])
    login_page.fill_code(code)


def like(name_convo, appium):
    navigation_bar = NavigationBar(appium)
    navigation_bar.click_navigation_bar_search()
    search_page = SearchPage(appium)
    search_page.click_search_field()
    search_page.click_convos_tab_button()
    search_page.fill_search(name_convo)
    search_page.click_search_result_convos(name_convo)
    detail_screen = DetailConvoScreenPage(appium)
    detail_screen.click_play_convo()
    player = FullScreenPlayerPage(appium)
    sleep(5)
    player.click_like_button()
    player.click_back_button()


def create_convo_thought(appium, last):
    record = RecordPage(appium)
    review = ReviewConvoPage(appium)
    record.click_start_record_button()
    sleep(5)
    record.click_stop_record()
    record.click_next_button()
    if not last:
        review.click_plus_record_button()


def create_convo_with_thoughts(appium, thoughts_count):
    navigation_bar = NavigationBar(appium)
    navigation_bar.click_navigation_bar_home()
    home = HomePage(appium)
    home.click_record_button()
    sleep(10)

    for i in range(thoughts_count):
        create_convo_thought(appium, i + 1 == thoughts_count)

    review = ReviewConvoPage(appium)
    review.click_share_button()
    share = ShareConvoPage(appium)
    share.click_title_field()
    title = generate_random_first_name()
    share.fill_title_field(title)
    share.click_back_button()
    review.click_share_button()
    share.click_share_button()
    return {
        'title': title,
    }


def create_convo(appium):
    navigation_bar = NavigationBar(appium)
    navigation_bar.click_navigation_bar_home()
    home = HomePage(appium)
    home.click_record_button()
    sleep(10)
    record = RecordPage(appium)
    record.click_start_record_button()
    sleep(20)
    record.click_stop_record()
    record.click_next_button()
    review = ReviewConvoPage(appium)
    review.click_share_button()
    share = ShareConvoPage(appium)
    share.click_title_field()
    title = generate_random_first_name()
    share.fill_title_field(title)
    share.click_share_button()
    return {
        'title': title,
    }


def create_convo_5min(appium):
    navigation_bar = NavigationBar(appium)
    navigation_bar.click_navigation_bar_home()
    home = HomePage(appium)
    home.click_record_button()
    sleep(10)
    record = RecordPage(appium)
    record.click_start_record_button()
    sleep(310)
    record.click_next_button()
    review = ReviewConvoPage(appium)
    review.click_share_button()
    share = ShareConvoPage(appium)
    share.click_title_field()
    title = generate_random_first_name()
    share.fill_title_field(title)
    share.click_back_button()
    review.click_share_button()
    share.click_share_button()
    return {
        'title': title,
    }


def create_replay(appium):
    create_convo(appium)
    sleep(5)
    navigation_bar = NavigationBar(appium)
    navigation_bar.click_navigation_bar_profile()
    profile = ProfilePage(appium)
    profile.click_last_convo()
    detail_convo = DetailConvoScreenPage(appium)
    detail_convo.click_play_convo()
    player = FullScreenPlayerPage(appium)
    player.click_reply_button()
    record = RecordPage(appium)
    record.click_start_record_button()
    sleep(5)
    record.click_stop_record()
    record.click_next_button()
    sleep(10)
    review = ReviewConvoPage(appium)
    review.clear_description_field()
    review.click_description_field()
    description = generate_random_description()
    review.fill_description_field(description)
    review.click_done_keyboard_button()
    review.click_share_button()
    player.click_back_button()
    detail_convo.click_back_button()
    return {
        'description': description,
    }
