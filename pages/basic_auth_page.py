from pages.base_page import BasePage
from elements.label import Label


class BasicAuthPage(BasePage):
    RESULT_LABEL_LOC = "//*[@id='content']//p"

    def __init__(self, driver):
        super().__init__(driver)

        self.result_label = Label(self.driver, self.RESULT_LABEL_LOC,
                                   description="Login page -> Result label")

    def get_text_result(self):
        return self.result_label.get_text()
