import time

from pages.base_page import BasePage
from elements.input import Input
from elements.label import Label
from elements.button import Button


class UploadImgPage(BasePage):
    UNIQUE_LOC_1 = "file-upload"

    UPLOAD_INPUT_LOC = "file-upload"
    SUBMIT_INPUT_LOC = "file-submit"
    TITLE_LABEL_LOC = "//*[@id='content']//h3"
    FILENAME_LABEL_LOC = "uploaded-files"

    DROP_UPLOAD_BUTTON_LOC = "drag-drop-upload"

    FILENAME_WINDOW_LABEL_LOC = "//*[@id='drag-drop-upload']" \
                                "//div[@class='dz-filename']//span"
    CHECK_MARK_LABEL_LOC = "//*[@id='drag-drop-upload']" \
                           "//div[@class='dz-success-mark']//span"

    def __init__(self, driver):
        super().__init__(driver)

        self.unique_element = Input(
            self.driver,
            self.UNIQUE_LOC_1,
            description="Upload img page -> Upload input"
        )

        self.upload_input = Input(
            self.driver,
            self.UPLOAD_INPUT_LOC,
            description="Upload img page -> Upload input"
        )
        self.submit_input = Input(
            self.driver,
            self.SUBMIT_INPUT_LOC,
            description="Upload img page -> Submit input"
        )
        self.title_label = Label(
            self.driver,
            self.TITLE_LABEL_LOC,
            description="Upload img page -> Title label"
        )
        self.filename_label = Label(
            self.driver,
            self.FILENAME_LABEL_LOC,
            description="Upload img page -> File name label"
        )

        self.drop_upload_button = Button(
            self.driver,
            self.DROP_UPLOAD_BUTTON_LOC,
            description="Upload img page -> Drop upload button"
        )

        self.filename_window_label = Label(
            self.driver,
            self.FILENAME_WINDOW_LABEL_LOC,
            description="Upload img page -> File name label"
        )
        self.check_mark_label = Label(
            self.driver,
            self.CHECK_MARK_LABEL_LOC,
            description="Upload img page -> Check mark label"
        )

    def upload_file(self, file):
        self.upload_input.send_keys(file)

    def submit_file(self):
        self.submit_input.click()

    def check_new_page(self):
        self.filename_label.wait_presence()

    def get_title_name(self):
        return self.title_label.get_text()

    def get_file_name(self):
        return self.filename_label.get_text()

    def click_upload_file(self):
        self.drop_upload_button.click()

    def get_file_name_2(self):
        return self.filename_window_label.get_text()

    def check_mark_is_displayed(self):
        return self.check_mark_label.is_displayed()
