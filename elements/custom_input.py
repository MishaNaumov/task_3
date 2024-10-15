from elements.input import Input
from selenium.webdriver.common.keys import Keys
from logging_test.logger import Logger


class CustomInput(Input):
    def select_all_text(self):
        self.click_js()
        Logger().info(f"{self.description}: select all text")
        self.wait_visibility().send_keys(Keys.CONTROL, "a")

    def select_all_text_bold(self):
        self.select_all_text()
        Logger().info(f"{self.description}: select all text bold")
        self.wait_visibility().send_keys(Keys.CONTROL, "b")

    def clear_format(self):
        self.select_all_text()
        Logger().info(f"{self.description}: clear format")
        self.wait_visibility().send_keys(Keys.CONTROL, Keys.SHIFT, "r")
