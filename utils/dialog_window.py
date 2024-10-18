import pyautogui
import selenium.common


class DialogWindow:
    @staticmethod
    def write(file):
        pyautogui.write(file, interval=0.25)

    @staticmethod
    def enter():
        pyautogui.press("enter")

    @classmethod
    def is_opened_dialog_window(cls, file):
        try:
            cls.write(file)
            return True
        except selenium.common.TimeoutException:
            return False
