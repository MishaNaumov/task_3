from utils.config_utils import ConfigUtils
from pages.dynamic_content_page import DynamicContentPage


def test_dynamic_content(driver):
    driver.get(ConfigUtils.get_attribute("url_dynamic_content_10"))
    dynamic_content_page = DynamicContentPage(driver)
    dynamic_content_page.wait_for_open()

    dynamic_content_page.refresh_page_for_2_img()

    assert dynamic_content_page.is_2_img_corrected(), "2 img do not match"
