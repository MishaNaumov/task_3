from utils.config_utils import ConfigUtils
from pages.upload_img_page import UploadImgPage
from utils.dialog_window import DialogWindow
import pytest
import os.path


@pytest.mark.parametrize("param", ["photo.png"])
def test_upload_img_and_dialog_window(driver, param):
    file = param
    driver.get(ConfigUtils.get_attribute("url_upload_image_12_13_14"))
    upload_img_page = UploadImgPage(driver)
    upload_img_page.wait_for_open()

    upload_img_page.click_upload_file()

    assert DialogWindow.is_opened_dialog_window(
        f"C{os.getcwd()}\photo\{file}"), "Dialog window did not open"

    DialogWindow.enter()

    file_name = upload_img_page.get_file_name_2()

    assert file_name == file, f"{file_name} File name not corrected"
    assert upload_img_page.check_mark_is_displayed(), "There is not check mark"
