from pages.base_page import BasePage
from elements.input import Input
from elements.label import Label
import selenium.common
import os


class UploadImgPage(BasePage):
    UNIQUE_LOC = "//*[@id='file-upload']"

    UPLOAD_INPUT_LOC = "//*[@id='file-upload']"
    SUBMIT_INPUT_LOC = "//*[@id='file-submit']"
    TITLE_LABEL_LOC = "//*[@id='content']//h3"
    FILENAME_LABEL_LOC = "//*[@id='uploaded-files']"

    def __init__(self, driver):
        super().__init__(driver)

        self.unique_element = Input(self.driver, self.UNIQUE_LOC,
                                   description="Upload img page -> Upload input")

        self.upload_input = Input(self.driver, self.UPLOAD_INPUT_LOC,
                                     description="Upload img page -> Upload input")
        self.submit_input = Input(self.driver, self.SUBMIT_INPUT_LOC,
                                  description="Upload img page -> Submit input")
        self.title_label = Label(self.driver, self.TITLE_LABEL_LOC,
                                  description="Upload img page -> Title label")
        self.filename_label = Label(self.driver, self.FILENAME_LABEL_LOC,
                                 description="Upload img page -> File name label")

    def upload_file(self, file):
        self.upload_input.send_keys(f"{os.getcwd()}/{file}")

    def submit_file(self):
        self.submit_input.click()

    def check_new_page(self):
        try:
            self.unique_element.presence_wait()
            return False
        except selenium.common.TimeoutException:
            return True

    def get_title_name(self):
        return self.title_label.get_text()

    def get_file_name(self):
        return self.filename_label.get_text()
