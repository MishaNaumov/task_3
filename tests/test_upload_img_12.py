from utils.config_utils import ConfigUtils
from pages.upload_img_page import UploadImgPage
import pytest
import os


@pytest.mark.parametrize("param", ["photo.png"])
def test_upload_img(driver, param):
    file = param
    driver.get(ConfigUtils.get_attribute("url_upload_image_12_13"))
    upload_img_page = UploadImgPage(driver)
    upload_img_page.wait_for_open()

    upload_img_page.upload_file(f"{os.getcwd()}/photo/{file}")
    upload_img_page.submit_file()

    upload_img_page.check_new_page()

    title_name = upload_img_page.get_title_name()
    assert title_name == "File Uploaded!", f"{title_name} Title not corrected"

    file_name = upload_img_page.get_file_name()
    assert file_name == file, f"{file_name} File name not corrected"
