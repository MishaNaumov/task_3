from utils.config_utils import ConfigUtils
from pages.iframe2_page import Iframe2Page


def test_iframe_plus(driver):
    driver.get(ConfigUtils.get_attribute("url_IFrame_image_15"))
    iframe_page = Iframe2Page(driver)
    iframe_page.wait_for_open()

    iframe_page.click_nest_frame()

    text_title_nest_frame = iframe_page.get_text_title_nest_frame()
    assert text_title_nest_frame == "Nested Frames", \
        f"{text_title_nest_frame} Title name not corrected"

    iframe_page.switch_iframe1_page1()
    page1_iframe1_text = iframe_page.get_text_iframe1_page1()
    assert page1_iframe1_text == "Parent frame",\
        f"{page1_iframe1_text} Text not corrected"

    iframe_page.switch_iframe2_page1()
    page1_iframe2_text = iframe_page.get_text_iframe2_page1()
    assert page1_iframe2_text == "Child Iframe",\
        f"{page1_iframe2_text} Text not corrected"

    driver.switch_to_default_content()
    iframe_page.click_frame()

    text_title_frame = iframe_page.get_text_title_frame()
    assert text_title_frame == "Frames",\
        f"{text_title_frame} Title name not corrected"

    iframe_page.switch_iframe1_page2()
    page2_iframe1_text = iframe_page.get_text_iframe1_page2()
    driver.switch_to_default_content()
    iframe_page.switch_iframe2_page2()
    page2_iframe2_text = iframe_page.get_text_iframe2_page2()
    driver.switch_to_default_content()

    assert page2_iframe1_text == page2_iframe2_text,\
        f"{page2_iframe1_text} and {page2_iframe2_text} - Texts dont match"
