from elements.base_element import BaseElement
from logging_test.logger import Logger


class Input(BaseElement):
    def send_keys(self, text):
        Logger().info(f"{self.description}: send keys")
        self.wait_visibility().send_keys(text)

    def clear(self):
        Logger().info(f"{self.description}: clear")
        self.wait_visibility().clear()
