from utils.json_utils import JsonUtils
from pages.alerts_page import AlertsPage


def test_alerts(driver):
    driver.get(JsonUtils.get_attribute("url_alerts_2_3"))
    alerts_page = AlertsPage(driver)
    alerts_page.wait_for_open()

    alerts_page.click_js_alert()
    text_alert_1 = driver.get_text()

    assert text_alert_1 == "I am a JS Alert", \
        f"{text_alert_1} The text is missing"

    driver.confirm()
    text_result_1 = alerts_page.get_text_result()

    assert text_result_1 == "You successfully clicked an alert", \
        f"{text_result_1} The text is missing"

    alerts_page.click_js_confirm()
    text_alert_2 = driver.get_text()

    assert text_alert_2 == "I am a JS Confirm", \
        f"{text_alert_2} The text is missing"

    driver.confirm()
    text_result_2 = alerts_page.get_text_result()

    assert text_result_2 == "You clicked: Ok", \
        f"{text_result_2} The text is missing"

    alerts_page.click_js_prompt()
    text_alert_3 = driver.get_text()

    assert text_alert_3 == "I am a JS prompt", \
        f"{text_alert_3} The text is missing"

    text = driver.write_text_and_confirm()
    text_result_3 = alerts_page.get_text_result()

    assert text_result_3 == f"You entered: {text}", \
        f"{text_result_3} The text is missing"