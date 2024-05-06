from page_models.library_page import LibraryPage
from page_models.navigation_bar import NavigationBar
from page_models.search_page import SearchPage
from page_models.user_pod_page import UserPodPage
from utills.action_utills import sign_up_following


def test_pod_subscribe_unsubscribe(appium):
    user = sign_up_following(appium)
    navigation_bar = NavigationBar(appium)
    navigation_bar.click_navigation_bar_search()
    search = SearchPage(appium)
    search.click_pods_tab_button()
    search.click_search_field()
    search.fill_search('Autotest_pod')
    search.wait(2)
    search.click_search_result_pods('Autotest_pod')
    pod = UserPodPage(appium)
    pod.click_follow_button()
    convos_names = pod.get_convos_names()
    navigation_bar.click_navigation_bar_library()
    library = LibraryPage(appium)
    library.click_latest_convos_tab()
    assert convos_names == library.get_convos_names()
    library.click_pods_you_follow_tab()
    assert 'Autotest_pod' == library.get_first_pod_name()

