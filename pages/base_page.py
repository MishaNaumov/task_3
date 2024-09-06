from utils.json_utils import JsonUtils
import selenium.common
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By


class BasePage:
    UNIQUE_LOC = None # Should be overwritten!

    def __init__(self, driver):
        self.driver = driver

    def is_page_opened(self):
        try:
            WebDriverWait(self.driver.driver, JsonUtils.get_attribute("timeout"))\
                .until(EC.presence_of_element_located(
                (By.XPATH, self.UNIQUE_LOC)))
            return True
        except selenium.common.TimeoutException:
            return False

