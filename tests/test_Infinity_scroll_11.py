import time

from utils.json_utils import JsonUtils
from pages.infinity_scroll_page import InfinityScrollPage


def test_alerts(driver):
    driver.get(JsonUtils.get_attribute("url_infinity_scroll_11"))
    infinity_scroll_page = InfinityScrollPage(driver)
    infinity_scroll_page.wait_for_open()

    infinity_scroll_page.scroll()
    time.sleep(2)

