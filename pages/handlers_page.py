from pages.base_page import BasePage
from elements.label import Label


class HandlersPage(BasePage):
    UNIQUE_LOC = "//*[@id='content']//a"

    CLICKER_LABEL_LOC = "//*[@id='content']//a"
    TEXT_LABEL = "//h3"

    def __init__(self, driver):
        super().__init__(driver)

        self.unique_element = Label(self.driver, self.UNIQUE_LOC,
                                   description="Handlers page -> Clicker label")

        self.clicker_label = Label(self.driver, self.CLICKER_LABEL_LOC,
                                   description="Handlers page -> Clicker label")
        self.text_label = Label(self.driver, self.TEXT_LABEL,
                                   description="Handlers page -> New window")

    def click_here(self):
        self.clicker_label.click()

    def is_new_window(self):
        if self.text_label.get_text() == "New Window" == \
                self.driver.get_title_widow():
            return True
        else:
            return False

    def close_window_1(self):
        self.driver.driver.switch_to.window(self.driver.driver.window_handles[-2])
        self.driver.driver.close()

    def close_window_2(self):
        self.driver.driver.switch_to.window(self.driver.driver.window_handles[-1])
        self.driver.driver.close()

    def is_page_closed_1(self):
        if len(self.driver.driver.window_handles) == 2:
            return True
        else:
            return False

    def is_page_closed_2(self):
        if len(self.driver.driver.window_handles) == 1:
            return True
        else:
            return False
