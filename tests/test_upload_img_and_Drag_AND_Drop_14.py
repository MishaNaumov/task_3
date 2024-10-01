from utils.config_utils import JsonUtils
from pages.upload_img_page import UploadImgPage
from utils.dialog_window import DialogWindow


FILE = "photo.png"
FILE_PATH = r"C:\Users\79119\task_3"


def test_alerts(driver):
    driver.get(JsonUtils.get_attribute("url_upload_image_12_13_14"))
    upload_img_page = UploadImgPage(driver)
    upload_img_page.wait_for_open()

    DialogWindow.open_dialog_window(FILE_PATH)
    DialogWindow.move_file()

    file_name = upload_img_page.get_file_name_2()

    assert file_name == FILE, f"{file_name} File name not corrected"
    assert upload_img_page.check_mark_is_displayed(), "There is not check mark"
