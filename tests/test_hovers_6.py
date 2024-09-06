from utils.json_utils import JsonUtils
from pages.hovers_page import HoversPage


def test_alerts(driver):
    driver.get(JsonUtils.get_attribute("url_hovers_6"))
    hovers_page = HoversPage(driver)

    assert hovers_page.is_page_opened, "Page not opened"
