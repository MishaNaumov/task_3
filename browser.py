from selenium import webdriver
import random
import string


class Browser:

    def __init__(self, options):
        self.driver = webdriver.Chrome(options)

    def get(self, url):
        return self.driver.get(url)

    def quit(self):
        self.driver.quit()

    def close(self):
        self.driver.close()

    def back_page(self):
        self.driver.back()

    def get_url(self):
        return self.driver.current_url

    def switch_active_window(self):
        self.driver.switch_to.window(self.driver.window_handles[-1])

    def switch_back_window(self):
        self.driver.switch_to.window(self.driver.window_handles[0])

    def get_title_widow(self):
        self.switch_active_window()
        return self.driver.title

    def alert(self):
        return self.driver.switch_to.alert

    def get_text(self):
        return self.alert().text

    def cancel(self):
        self.alert().dismiss()

    def write_text_and_confirm(self):
        text = ''.join(
            [random.choice(string.ascii_lowercase + string.digits
                           if i != 5 else string.ascii_uppercase)
             for i in range(10)])
        self.alert().send_keys(text)
        self.confirm()
        return text

    def confirm(self):
        self.alert().accept()
