from elements.base_element import BaseElement
from selenium.webdriver.common.keys import Keys


class Input(BaseElement):
    def send_keys(self, text):
        self.visibility_wait().send_keys(text)

    def clear(self):
        self.visibility_wait().clear()

    def select_all_text(self):
        self.visibility_wait().send_keys(Keys.CONTROL, "a")

    def select_all_text_bold(self):
        self.visibility_wait().send_keys(Keys.CONTROL, "a")
        self.visibility_wait().send_keys(Keys.CONTROL, "b")

    def clear_format(self):
        self.visibility_wait().send_keys(Keys.CONTROL, "a")
        self.visibility_wait().send_keys(Keys.CONTROL, Keys.SHIFT, "r")
