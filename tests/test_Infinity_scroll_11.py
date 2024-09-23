from utils.json_utils import JsonUtils
from pages.infinity_scroll_page import InfinityScrollPage

AGE = 23


def test_alerts(driver):
    driver.get(JsonUtils.get_attribute("url_infinity_scroll_11"))
    infinity_scroll_page = InfinityScrollPage(driver)
    infinity_scroll_page.wait_for_open()

    count_paragraph = infinity_scroll_page.scroll()

    assert count_paragraph == AGE,\
        f"{count_paragraph} The number of paragraphs does not match the age"



