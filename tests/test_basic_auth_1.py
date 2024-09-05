import time

from utils.json_utils import JsonUtils
from pages.basic_auth_page import BasicAuthPage


def test_basic_auth(driver):
    username = "admin"
    password = "admin"
    driver.get(JsonUtils.get_attribute("url_basic_authorization_1")
               .format(username, password))
    authorization_page = BasicAuthPage(driver)

    assert authorization_page.get_text_result() == \
           "Congratulations! You must have the proper credentials.", \
        "Basic Authorization page not opened"
