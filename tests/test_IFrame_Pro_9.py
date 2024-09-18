from utils.json_utils import JsonUtils
from pages.iframe_page import IframePage


def test_alerts(driver):
    driver.get(JsonUtils.get_attribute("url_IFrame_8_9"))
    iframe_page = IframePage(driver)
    iframe_page.wait_for_open()

    iframe_page.switch_iframe1()

    iframe_page.clear_field()
    iframe_page.send_keys_random()
    iframe_page.select_all_text()

    driver.quit_frame()
    iframe_page.align_text_right()

    iframe_page.switch_iframe1()
    style_text = iframe_page.get_style_text()

    assert style_text == "right", "Text not on right side"

    iframe_page.select_half_text()
    driver.quit_frame()
    iframe_page.turn_text_8pt()

    iframe_page.switch_iframe1()
    font_size_text = iframe_page.get_font_size_text()

    assert font_size_text == "8pt", "Text is not 8pt"

    iframe_page.new_file()
    text_iframe = iframe_page.get_text()

    assert text_iframe == "", "Iframe not cleared"
    assert iframe_page.is_clear_format()
    driver.quit_frame()
