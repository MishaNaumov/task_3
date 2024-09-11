from utils.json_utils import JsonUtils
from pages.hovers_page import HoversPage


def test_alerts(driver):
    driver.get(JsonUtils.get_attribute("url_hovers_6"))
    hovers_page = HoversPage(driver)
    hovers_page.wait_for_open()

    hovers_page.move_to_img1()
    assert hovers_page.is_img_1_corrected()
    hovers_page.click_for_img1()
    assert hovers_page.is_url1_corrected()
    driver.back_page()
    assert hovers_page.is_page_opened()

    hovers_page.move_to_img2()
    assert hovers_page.is_img_2_corrected()
    hovers_page.click_for_img2()
    assert hovers_page.is_url2_corrected()
    driver.back_page()
    assert hovers_page.is_page_opened()

    hovers_page.move_to_img3()
    assert hovers_page.is_img_3_corrected()
    hovers_page.click_for_img3()
    assert hovers_page.is_url3_corrected()
    driver.back_page()
    assert hovers_page.is_page_opened()
