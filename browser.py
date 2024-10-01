from utils.random_utils import RandomUtils
from logging_test.logger import Logger
from browser_factory import BrowserFactory


class Browser:

    def __init__(self):
        self.driver = BrowserFactory.get_browser_instance()

    def get(self, url):
        Logger().info("login browser")
        return self.driver.get(url)

    def quit(self):
        Logger().info("quit browser")
        self.driver.quit()

    def close(self):
        Logger().info("close")
        self.driver.close()

    def back_page(self):
        Logger().info("return to previous page")
        self.driver.back()

    def get_url(self):
        Logger().info("getting url")
        return self.driver.current_url

    def refresh(self):
        Logger().info("refresh page")
        self.driver.refresh()

    def get_page_source(self):
        Logger().info("getting page source")
        return self.driver.page_source

    def click_js(self, element):
        Logger().info("click js")
        self.driver.execute_script("arguments[0].click();", element)

    def scroll_down(self, element):
        Logger().info("scroll down")
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def switch_active_window(self):
        Logger().info("switch last window")
        self.driver.switch_to.window(self.driver.window_handles[-1])

    def switch_first_window(self):
        Logger().info("switch first window")
        self.driver.switch_to.window(self.driver.window_handles[-2])

    def switch_second_window(self):
        Logger().info("switch second window")
        self.driver.switch_to.window(self.driver.window_handles[-1])

    def switch_back_window(self):
        Logger().info("switch back window")
        self.driver.switch_to.window(self.driver.window_handles[0])

    def get_title_window(self):
        self.switch_active_window()
        Logger().info("getting title window")
        return self.driver.title

    def frame(self, iframe):
        Logger().info("switch iframe")
        self.driver.switch_to.frame(iframe)

    def quit_frame(self):
        Logger().info("quit iframe")
        self.driver.switch_to.default_content()

    def alert(self):
        Logger().info("switch alert")
        return self.driver.switch_to.alert

    def get_text(self):
        Logger().info("driver getting text")
        return self.alert().text

    def cancel(self):
        Logger().info("cancel")
        self.alert().dismiss()

    def write_text_and_confirm(self):
        text = RandomUtils().random_str(10)
        self.alert().send_keys(text)
        self.confirm()
        Logger().info("writing text and confirm")
        return text

    def confirm(self):
        Logger().info("confirm")
        self.alert().accept()
