from logger.logger import Logger
from browser_factory import BrowserFactory
from selenium.webdriver.support.wait import WebDriverWait
from utils.config_utils import ConfigUtils
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.support import expected_conditions as EC


class Browser:

    def __init__(self):
        self.driver = BrowserFactory.get_browser_instance()

    def get(self, url):
        Logger.info("Login browser")
        self.driver.get(url)

    def quit(self):
        Logger.info("Quit browser")
        self.driver.quit()

    def close(self):
        Logger.info("Close")
        self.driver.close()

    def back(self):
        Logger.info("Back")
        self.driver.back()

    def get_url(self):
        Logger.info("Get url")
        return self.driver.current_url

    def refresh(self):
        Logger.info("Refresh page")
        self.driver.refresh()

    def switch_window(self, index):
        Logger.info(f"Switch {index} window")
        self.driver.switch_to.window(self.driver.window_handles[index])

    def get_title_window(self):
        Logger.info("Get title window")
        return self.driver.title

    def switch_frame(self, frame):
        Logger.info("Switch frame")
        self.driver.switch_to.frame(frame)

    def switch_to_default_content(self):
        Logger.info("Switch to default content")
        self.driver.switch_to.default_content()

    def switch_alert(self):
        Logger.info("Switch alert")
        wait = WebDriverWait(self.driver, ConfigUtils.get_attribute("timeout"))
        alert = wait.until(EC.alert_is_present())
        return alert

    def is_alert_closed(self):
        try:
            self.switch_alert()
            return False
        except NoAlertPresentException:
            return True

    def get_text_alert(self):
        Logger.info("Get text alert")
        return self.switch_alert().text

    def cancel_alert(self):
        Logger.info("Cancel alert")
        self.switch_alert().dismiss()

    def write_text_and_confirm(self, text):
        self.switch_alert().send_keys(text)
        self.confirm_alert()
        Logger.info("Write text and confirm")
        return text

    def confirm_alert(self):
        Logger.info("Confirm alert")
        self.switch_alert().accept()
