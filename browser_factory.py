from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from utils.config_utils import ConfigUtils


class BrowserFactory:

    @staticmethod
    def get_browser_instance():
        options = Options()
        for item in ConfigUtils.get_attribute("options"):
            options.add_argument(item)
        return webdriver.Chrome(options)

