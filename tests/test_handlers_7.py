import time

from utils.json_utils import JsonUtils
from pages.handlers_page import HandlersPage


def test_alerts(driver):
    driver.get(JsonUtils.get_attribute("url_handlers_7"))
    handlers_page = HandlersPage(driver)

    handlers_page.wait_for_open()

    handlers_page.click_here()

    assert handlers_page.is_new_window()

    driver.switch_back_window()

    assert handlers_page.is_page_opened()

    handlers_page.click_here()

    assert handlers_page.is_new_window()

    driver.switch_back_window()

    assert handlers_page.is_page_opened()

    handlers_page.close_window_1()

    assert handlers_page.is_page_closed_1()

    handlers_page.close_window_2()

    assert handlers_page.is_page_closed_2()





