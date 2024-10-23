from utils.config_utils import ConfigUtils
from pages.iframe_page import IframePage
from utils.random_utils import RandomUtils
from utils.dict_utils import DictUtils


def test_iframe_pro(driver):
    driver.get(ConfigUtils.get_attribute("url_IFrame_8_9"))
    iframe_page = IframePage(driver)
    iframe_page.wait_for_open()

    iframe_page.switch_iframe1()

    iframe_page.clear_field_iframe()
    iframe_page.send_keys_random(RandomUtils().random_str(20))
    iframe_page.select_all_text()

    driver.switch_to_default_content()
    iframe_page.align_text_right()

    iframe_page.switch_iframe1()
    style_text = iframe_page.get_style_text()
    style_dict = DictUtils.get_value(style_text)

    assert style_dict["text-align"] == "right", "Text not on right side"

    iframe_page.select_half_text()
    driver.switch_to_default_content()
    iframe_page.turn_text_8pt()

    iframe_page.switch_iframe1()
    font_size_text = iframe_page.get_font_size_text()
    font_size_dict = DictUtils.get_value(font_size_text)

    assert font_size_dict["font-size"] == "8pt", "Text is not 8pt"

    iframe_page.create_new_file()
    text_iframe = iframe_page.get_text()

    assert not text_iframe
    assert iframe_page.is_clear_format()
    driver.switch_to_default_content()
