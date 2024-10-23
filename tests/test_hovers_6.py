from utils.config_utils import ConfigUtils
from pages.hovers_page import HoversPage


def test_hovers(driver):
    driver.get(ConfigUtils.get_attribute("url_hovers_6"))
    hovers_page = HoversPage(driver)
    hovers_page.wait_for_open()

    hovers_page.move_to_img(1)
    img1_text = hovers_page.get_text_img(1).split(":")[-1].strip()
    assert img1_text == "user1", f"{img1_text} Incorrect username is displayed"
    hovers_page.click_img(1)
    img1_url = driver.get_url().split("/")[-1]
    assert img1_url == "1", "The link was not opened for that user"
    driver.back()
    hovers_page.wait_for_open()

    hovers_page.move_to_img(2)
    img2_text = hovers_page.get_text_img(2).split(":")[-1].strip()
    assert img2_text == "user2", f"{img2_text} Incorrect username is displayed"
    hovers_page.click_img(2)
    img2_url = driver.get_url().split("/")[-1]
    assert img2_url == "2", "The link was not opened for that user"
    driver.back()
    hovers_page.wait_for_open()

    hovers_page.move_to_img(3)
    img3_text = hovers_page.get_text_img(3).split(":")[-1].strip()
    assert img3_text == "user3", f"{img3_text} Incorrect username is displayed"
    hovers_page.click_img(3)
    img3_url = driver.get_url().split("/")[-1]
    assert img3_url == "3", "The link was not opened for that user"
    driver.back()
    hovers_page.wait_for_open()
