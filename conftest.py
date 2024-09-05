from selenium.webdriver.chrome.options import Options
from utils.json_utils import JsonUtils
from browser import Browser


import pytest


@pytest.fixture()
def driver():
    options = Options()
    for item in JsonUtils.get_attribute("options"):
        options.add_argument(item)
    web_chrome = Browser(options)

    return web_chrome
