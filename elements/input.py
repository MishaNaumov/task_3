from elements.base_element import BaseElement
from selenium.webdriver.common.keys import Keys
from logging_test.logger import Logger


class Input(BaseElement):
    def send_keys(self, text):
        Logger().info(f"{self.description}: send keys")
        self.visibility_wait().send_keys(text)

    def clear(self):
        Logger().info(f"{self.description}: clear")
        self.visibility_wait().clear()

    def select_all_text(self):
        Logger().info(f"{self.description}: select all text")
        self.visibility_wait().send_keys(Keys.CONTROL, "a")

    def select_all_text_bold(self):
        self.select_all_text()
        Logger().info(f"{self.description}: select all text bold")
        self.visibility_wait().send_keys(Keys.CONTROL, "b")

    def clear_format(self):
        self.select_all_text()
        Logger().info(f"{self.description}: clear format")
        self.visibility_wait().send_keys(Keys.CONTROL, Keys.SHIFT, "r")
