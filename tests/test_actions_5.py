from utils.json_utils import JsonUtils
from pages.actions_page import ActionsPage


def test_actions(driver):
    driver.get(JsonUtils.get_attribute("url_actions_5"))
    actions_page = ActionsPage(driver)

    assert actions_page.is_page_opened, "Page not opened"

    value = actions_page.random_value()

    assert value == actions_page.check_value(), "Incorrect value is displayed"
