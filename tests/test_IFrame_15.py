from utils.config_utils import JsonUtils
from pages.iframe2_page import Iframe2Page


def test_alerts(driver):
    driver.get(JsonUtils.get_attribute("url_IFrame_image_15"))
    iframe_page = Iframe2Page(driver)
    iframe_page.wait_for_open()

    iframe_page.click_nest_frame()

    text_title_nest_frame = iframe_page.get_text_title_nest_frame()
    assert text_title_nest_frame == "Nested Frames", \
        f"{text_title_nest_frame} Title name not corrected"

    iframe_page.page1_switch_iframe1()
    page1_iframe1_text = iframe_page.get_text_page1_iframe1()
    assert page1_iframe1_text == "Parent frame",\
        f"{page1_iframe1_text} Text not corrected"

    iframe_page.page1_switch_iframe2()
    page1_iframe2_text = iframe_page.get_text_page1_iframe2()
    assert page1_iframe2_text == "Child Iframe",\
        f"{page1_iframe2_text} Text not corrected"

    driver.quit_frame()
    iframe_page.click_frame()

    text_title_frame = iframe_page.get_text_title_frame()
    assert text_title_frame == "Frames",\
        f"{text_title_frame} Title name not corrected"

    iframe_page.page2_switch_iframe1()
    page2_iframe1_text = iframe_page.get_text_page2_iframe1()
    driver.quit_frame()
    iframe_page.page2_switch_iframe2()
    page2_iframe2_text = iframe_page.get_text_page2_iframe2()
    driver.quit_frame()

    assert page2_iframe1_text == page2_iframe2_text, "Texts dont match"
