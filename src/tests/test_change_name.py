from page_models.profile_page import ProfilePage
from page_models.profile_settings_page import ProfileSettingsPage
from utills.action_utills import sign_up_following
from utills.random_utils import generate_random_first_name, generate_random_last_name
from time import sleep

def test_change_name(appium):
    user = sign_up_following(appium)
    profile = ProfilePage(appium)
    settings = ProfileSettingsPage(appium)
    sleep(5)
    profile.click_settings_button_profile()
    settings.click_name_field()
    settings.clear_first_name_field()
    first_name = generate_random_first_name()
    settings.fill_first_name_field(first_name)
    settings.clear_last_name_field()
    settings.click_edit_name()
    settings.click_last_name_field()
    last_name = generate_random_last_name()
    settings.fill_last_name_field(last_name)
    settings.click_update_button()
    sleep(2)
    settings.click_name_field()
    assert user['first_name'] != settings.get_first_name()
    assert user['last_name'] != settings.get_last_name()
    # тут такая гениальная хуйня написана почему: после изменения текста в элементах без перезахода в приложение, он не может понять что там что-то поменялось и всегда берёт старый текст и сравнивает с новым (всего то три часа понадобилось чтобы перебрать все варианты тут и понять это). Поэтому тут неравенство.