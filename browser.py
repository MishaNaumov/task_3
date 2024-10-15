from logging_test.logger import Logger
from browser_factory import BrowserFactory
from selenium.webdriver.support.wait import WebDriverWait
from utils.config_utils import ConfigUtils
from selenium.common.exceptions import NoAlertPresentException


class Browser:

    def __init__(self):
        self.driver = BrowserFactory.get_browser_instance()

    def get(self, url):
        Logger().info("login browser")
        self.driver.get(url)

    def quit(self):
        Logger().info("quit browser")
        self.driver.quit()

    def close(self):
        Logger().info("close")
        self.driver.close()

    def back(self):
        Logger().info("back")
        self.driver.back()

    def get_url(self):
        Logger().info("get url")
        return self.driver.current_url

    def refresh(self):
        Logger().info("refresh page")
        self.driver.refresh()

    def get_page_source(self):
        Logger().info("get page source")
        return self.driver.page_source

    def switch_last_window(self):
        Logger().info("switch last window")
        self.driver.switch_to.window(self.driver.window_handles[-1])

    def switch_penultimate_window(self):
        Logger().info("switch penultimate window")
        self.driver.switch_to.window(self.driver.window_handles[-2])

    def switch_first_window(self):
        Logger().info("switch first window")
        self.driver.switch_to.window(self.driver.window_handles[0])

    def get_title_window(self):
        self.switch_last_window()
        Logger().info("get title window")
        return self.driver.title

    def switch_frame(self, frame):
        Logger().info("switch frame")
        self.driver.switch_to.frame(frame)

    def switch_to_default_content(self):
        Logger().info("switch to default content")
        self.driver.switch_to.default_content()

    def switch_alert(self):
        Logger().info("switch alert")
        wait = WebDriverWait(self.driver, ConfigUtils.get_attribute("timeout"))
        alert = wait.until(lambda d: d.switch_to.alert)
        return alert

    def is_alert_closed(self):
        try:
            self.switch_alert()
            return False
        except NoAlertPresentException:
            return True

    def get_text(self):
        Logger().info("driver get text")
        return self.switch_alert().text

    def cancel(self):
        Logger().info("cancel")
        self.switch_alert().dismiss()

    def write_text_and_confirm(self, text):
        self.switch_alert().send_keys(text)
        self.confirm()
        Logger().info("write text and confirm")
        return text

    def confirm(self):
        Logger().info("confirm")
        self.switch_alert().accept()
