from utils.config_utils import ConfigUtils
from pages.actions_page import ActionsPage
from utils.random_utils import RandomUtils


def test_actions(driver):
    driver.get(ConfigUtils.get_attribute("url_actions_5"))
    actions_page = ActionsPage(driver)
    actions_page.wait_for_open()

    value = actions_page.move_action(RandomUtils.random_value())

    assert value == actions_page.get_value(), "Incorrect value is displayed"
