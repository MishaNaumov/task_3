from pages.alerts_and_context_click_page import AlertsContextPage
from utils.config_utils import ConfigUtils


def test_alerts_and_context_click(driver):
    driver.get(ConfigUtils.get_attribute("url_alerts_ContexClick_4"))
    alerts_context_page = AlertsContextPage(driver)
    alerts_context_page.wait_for_open()

    alerts_context_page.right_click_field()
    text_alert = driver.get_text()

    assert text_alert == "You selected a context menu",\
        f"{text_alert} The text is missing"

    driver.confirm()

    driver.is_alert_closed()
