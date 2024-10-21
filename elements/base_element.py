from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from utils.config_utils import ConfigUtils
from selenium.webdriver.common.by import By
from logger.logger import Logger


class BaseElement:
    def __init__(self, driver, loc, description):
        self.driver = driver
        self.loc = loc
        self.description = description

        if isinstance(loc, str):
            if "/" in loc:
                self.loc = (By.XPATH, loc)
            else:
                self.loc = (By.ID, loc)
        else:
            self.loc = loc

    def wait_clickable(self):
        return WebDriverWait(
            self.driver.driver, ConfigUtils.get_attribute("timeout")).until(
            EC.element_to_be_clickable(self.loc)
        )

    def wait_visibility(self):
        return WebDriverWait(
            self.driver.driver, ConfigUtils.get_attribute("timeout")).until(
            EC.visibility_of_element_located(self.loc)
        )

    def wait_presence(self):
        return WebDriverWait(
            self.driver.driver, ConfigUtils.get_attribute("timeout")).until(
            EC.presence_of_element_located(self.loc)
        )

    def click(self):
        Logger.info(f"{self.description}: click")
        self.wait_clickable().click()

    def click_js(self):
        Logger.info(f"{self.description}: сlick js")
        self.driver.driver.execute_script("arguments[0].click();",
                                          self.wait_presence())

    def scroll_down(self):
        Logger.info(f"{self.description}: scroll down")
        self.driver.driver.execute_script("arguments[0].scrollIntoView();",
                                          self.wait_presence())

    def get_text(self):
        Logger.info(f"{self.description}: get text")
        return self.wait_presence().text

    def is_displayed(self):
        Logger.info(f"{self.description}: visible on the display")
        return self.wait_presence().is_displayed()

    def get_attribute(self, arg):
        Logger.info(f"{self.description}: get attribute '{arg}'")
        return self.wait_presence().get_attribute(arg)

    def right_click(self):
        Logger.info(f"{self.description}: right click")
        ActionChains(self.driver.driver).context_click(
            self.wait_presence()).perform()

    def double_click(self):
        Logger.info(f"{self.description}: double click")
        ActionChains(self.driver.driver).double_click(
            self.wait_presence()).perform()

    def click_and_hold(self):
        Logger.info(f"{self.description}: click and hold")
        ActionChains(self.driver.driver).click_and_hold(
            self.wait_presence()).release().perform()

    def move_to_element(self):
        Logger.info(f"{self.description}: move to element")
        ActionChains(self.driver.driver).move_to_element(
            self.wait_presence()).perform()

    def key_down(self, arg):
        Logger.info(f"{self.description}: key down")
        ActionChains(self.driver.driver).key_down(arg).perform()
