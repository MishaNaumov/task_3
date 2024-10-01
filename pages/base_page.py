import selenium.common


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.unique_element = None

    def wait_for_open(self):
        self.unique_element.presence_wait()

    def is_page_opened(self):
        try:
            self.unique_element.presence_wait()
            return True
        except selenium.common.TimeoutException:
            return False
