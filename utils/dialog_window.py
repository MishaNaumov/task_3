import time
import pyautogui
import os
import selenium.common


class DialogWindow:
    PROGRAM = "explorer.exe"

    @staticmethod
    def write(file):
        pyautogui.write(file, interval=0.25)

    @staticmethod
    def enter():
        pyautogui.press("enter")

    @staticmethod
    def open_dialog_window(file):
        os.system(file)
        time.sleep(1)

    @staticmethod
    def move_file():
        pyautogui.moveTo(219, 252)
        pyautogui.dragTo(600, 750, 1, button='left')

    @classmethod
    def is_opened_dialog_window(cls, file):
        try:
            cls.write(file)
            return True
        except selenium.common.TimeoutException:
            return False

