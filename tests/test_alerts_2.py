from utils.json_utils import JsonUtils
from pages.alerts_page import AlertsPage


def test_alerts(driver):
    driver.get(JsonUtils.get_attribute("url_alerts_2_3"))
    alerts_page = AlertsPage(driver)

    assert alerts_page.is_page_opened, "Home page not opened"
