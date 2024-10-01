from utils.config_utils import JsonUtils
from pages.upload_img_page import UploadImgPage

FILE = "photo.png"


def test_alerts(driver):
    driver.get(JsonUtils.get_attribute("url_upload_image_12_13_14"))
    upload_img_page = UploadImgPage(driver)
    upload_img_page.wait_for_open()

    upload_img_page.upload_file(FILE)
    upload_img_page.submit_file()

    assert upload_img_page.check_new_page(), "Page not updated"

    title_name = upload_img_page.get_title_name()
    assert title_name == "File Uploaded!", f"{title_name} Title not corrected"

    file_name = upload_img_page.get_file_name()
    assert file_name == FILE, f"{file_name} File name not corrected"
