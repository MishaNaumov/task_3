from browser import Browser
import pytest


@pytest.fixture()
def driver():
    web_chrome = Browser()

    yield web_chrome
    web_chrome.quit()

