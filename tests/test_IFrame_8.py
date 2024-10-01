from utils.config_utils import JsonUtils
from pages.iframe_page import IframePage


def test_alerts(driver):
    driver.get(JsonUtils.get_attribute("url_IFrame_8_9"))
    iframe_page = IframePage(driver)
    iframe_page.wait_for_open()

    iframe_page.switch_iframe1()

    iframe_page.clear_field()
    send_text = iframe_page.send_keys_random()
    page_text = iframe_page.get_text()

    assert send_text == page_text, f"{send_text} The text is missing"

    iframe_page.select_all_text_bold()

    assert iframe_page.is_text_bold(), "The text is not bold"

    driver.quit_frame()
