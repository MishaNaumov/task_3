from utils.json_utils import JsonUtils
from pages.upload_img_page import UploadImgPage


def test_alerts(driver):
    driver.get(JsonUtils.get_attribute("url_upload_image_12_13_14"))
    upload_img_page = UploadImgPage(driver)
    upload_img_page.wait_for_open()

    file = "test.txt"
    upload_img_page.upload_file(file)
    upload_img_page.submit_file()

    assert upload_img_page.check_new_page(), "Page not updated"

    title_name = upload_img_page.get_title_name()
    assert title_name == "File Uploaded!", f"{title_name} Title not corrected"

    file_name = upload_img_page.get_file_name()
    assert file_name == file, f"{file_name} File name not corrected"
