from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from utils.json_utils import JsonUtils
from selenium.webdriver.common.by import By


class BaseElement:
    def __init__(self, driver, loc, description):
        self.driver = driver
        self.loc = loc
        self.description = description

    @property
    def clickable_wait(self):
        return WebDriverWait(self.driver.driver, JsonUtils.get_attribute("timeout"))\
            .until(EC.visibility_of_element_located((By.XPATH, self.loc)))

    @property
    def visibility_wait(self):
        return WebDriverWait(self.driver.driver, JsonUtils.get_attribute("timeout"))\
            .until(EC.visibility_of_element_located((By.XPATH, self.loc)))

    @property
    def presence_wait(self):
        return WebDriverWait(self.driver.driver, JsonUtils.get_attribute("timeout"))\
            .until(EC.visibility_of_element_located((By.XPATH, self.loc)))

    def click(self):
        self.clickable_wait.click()

    def right_click(self, element):
        temp = self.driver.driver.find_element(By.XPATH, element)
        action = ActionChains(self.driver.driver)
        action.context_click(temp).perform()

    def double_click(self, element):
        temp = self.driver.driver.find_element(By.XPATH, element)
        action = ActionChains(self.driver.driver)
        action.double_click(temp).perform()

    def get_text(self):
        return self.presence_wait.text

