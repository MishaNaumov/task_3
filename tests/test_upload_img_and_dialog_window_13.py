from utils.config_utils import ConfigUtils
from pages.upload_img_page import UploadImgPage
from utils.dialog_window_utils import DialogWindowUtils
import pytest
import os.path


@pytest.mark.parametrize("file", ["photo.png"])
def test_upload_img_and_dialog_window(driver, file):
    driver.get(ConfigUtils.get_attribute("url_upload_image_12_13"))
    upload_img_page = UploadImgPage(driver)
    upload_img_page.wait_for_open()

    upload_img_page.click_upload_file()

    DialogWindowUtils.write_and_enter(f"{os.getcwd()}\photo\{file}")

    file_name = upload_img_page.get_file_name_2()

    assert file_name == file, f"{file_name} File name not corrected"
    assert upload_img_page.check_mark_is_displayed(), "There is not check mark"
