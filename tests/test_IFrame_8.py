from utils.config_utils import ConfigUtils
from pages.iframe_page import IframePage
from utils.random_utils import RandomUtils


def test_iframe(driver):
    driver.get(ConfigUtils.get_attribute("url_IFrame_8_9"))
    iframe_page = IframePage(driver)
    iframe_page.wait_for_open()

    iframe_page.switch_iframe1()

    iframe_page.clear_field_iframe()
    send_text = RandomUtils().random_str(20)
    iframe_page.send_keys_random(send_text)
    page_text = iframe_page.get_text()

    assert send_text == page_text,\
        f"AR:{page_text} ER:{send_text} The text is missing"

    iframe_page.select_all_text_bold()

    assert iframe_page.is_text_bold(), "The text is not bold"

    driver.switch_to_default_content()
