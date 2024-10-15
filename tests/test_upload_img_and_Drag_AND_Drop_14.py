from utils.config_utils import ConfigUtils
from pages.upload_img_page import UploadImgPage
from utils.dialog_window import DialogWindow
import pytest
import os


@pytest.mark.parametrize("param", ["photo.png"])
def test_upload_img_and_drag_and_drop(driver, param):
    file = param
    driver.get(ConfigUtils.get_attribute("url_upload_image_12_13_14"))
    upload_img_page = UploadImgPage(driver)
    upload_img_page.wait_for_open()

    DialogWindow.open_dialog_window(fr"explorer.exe {os.getcwd()}\photo")
    DialogWindow.move_file()

    file_name = upload_img_page.get_file_name_2()

    assert file_name == file, f"{file_name} File name not corrected"
    assert upload_img_page.check_mark_is_displayed(), "There is not check mark"
