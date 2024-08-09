from selenium.webdriver.chrome.options import Options
from utils.json_utils import JsonUtils
# from webdriver import WebDriver
from selenium import webdriver

import pytest


@pytest.fixture()
def driver():
    options = Options()
    for item in JsonUtils.get_attribute("options"):
        options.add_argument(item)
    web_chrome = webdriver.Chrome(options)

    return web_chrome
    # yield web_chrome
    # WebDriver.quit()
