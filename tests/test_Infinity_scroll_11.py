from utils.config_utils import ConfigUtils
from pages.infinity_scroll_page import InfinityScrollPage
import pytest


@pytest.mark.parametrize("age", [23])
def test_infinity_scroll(driver, age):
    driver.get(ConfigUtils.get_attribute("url_infinity_scroll_11"))
    infinity_scroll_page = InfinityScrollPage(driver)
    infinity_scroll_page.wait_for_open()

    count_paragraph = infinity_scroll_page.scroll_until_paragraph(age)

    assert count_paragraph == age,\
        f"{count_paragraph} The number of paragraphs does not match the age"
