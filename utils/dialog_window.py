import time
import pyautogui
import os


class DialogWindow:
    @staticmethod
    def write(file):
        pyautogui.write(f"C{file}", interval=0.25)

    @staticmethod
    def enter():
        pyautogui.press("enter")

    @staticmethod
    def open_dialog_window(path):
        os.system(f"explorer.exe {path}")
        time.sleep(1)

    @staticmethod
    def move_file():
        pyautogui.moveTo(219, 542)
        pyautogui.dragTo(600, 750, 1, button='left')
