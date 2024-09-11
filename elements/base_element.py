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

    def clickable_wait(self):
        return WebDriverWait(self.driver.driver, JsonUtils.get_attribute("timeout"))\
            .until(EC.visibility_of_element_located((By.XPATH, self.loc)))

    def visibility_wait(self):
        return WebDriverWait(self.driver.driver, JsonUtils.get_attribute("timeout"))\
            .until(EC.visibility_of_element_located((By.XPATH, self.loc)))

    def presence_wait(self):
        return WebDriverWait(self.driver.driver, JsonUtils.get_attribute("timeout"))\
            .until(EC.visibility_of_element_located((By.XPATH, self.loc)))

    def click(self):
        self.clickable_wait().click()

    def get_text(self):
        self.driver.switch_active_window()
        return self.presence_wait().text

    def get_attribute(self, arg):
        return self.driver.driver.find_element(By.XPATH, self.loc).\
            get_attribute(arg)

    def right_click(self):
        temp = self.driver.driver.find_element(By.XPATH, self.loc)
        action = ActionChains(self.driver.driver)
        action.context_click(temp).perform()

    def double_click(self):
        temp = self.driver.driver.find_element(By.XPATH, self.loc)
        action = ActionChains(self.driver.driver)
        action.double_click(temp).perform()

    def click_and_hole(self, value):
        temp = self.driver.driver.find_element(By.XPATH, self.loc)
        action = ActionChains(self.driver.driver)
        action.click_and_hold(temp).move_by_offset(value, 0).release().perform()

    def move_to_element(self):
        temp = self.driver.driver.find_element(By.XPATH, self.loc)
        action = ActionChains(self.driver.driver)
        action.move_to_element(temp).perform()




