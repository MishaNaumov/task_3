from utils.json_utils import JsonUtils


def test_actions(driver):
    driver.get(JsonUtils.get_attribute("url_basic_authorization_1"))
