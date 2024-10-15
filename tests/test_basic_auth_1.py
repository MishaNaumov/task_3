from utils.config_utils import ConfigUtils
from pages.basic_auth_page import BasicAuthPage
import pytest


@pytest.mark.parametrize("param", [("admin", "admin")])
def test_basic_auth(driver, param):
    username, password = param
    driver.get(ConfigUtils.get_attribute("url_basic_authorization_1")
               .format(username, password))
    authorization_page = BasicAuthPage(driver)

    assert authorization_page.get_text_result() ==\
           "Congratulations! You must have the proper credentials.",\
        "Basic Authorization page not opened"
