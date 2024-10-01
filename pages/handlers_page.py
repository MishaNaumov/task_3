from pages.base_page import BasePage
from elements.label import Label


class HandlersPage(BasePage):
    UNIQUE_LOC = "//*[@id='content']//a"

    CLICKER_LABEL_LOC = "//*[@id='content']//a"
    TEXT_LABEL = "//h3"

    def __init__(self, driver):
        super().__init__(driver)

        self.unique_element = Label(
            self.driver,
            self.UNIQUE_LOC,
            description="Handlers page -> Clicker label"
        )

        self.clicker_label = Label(
            self.driver,
            self.CLICKER_LABEL_LOC,
            description="Handlers page -> Clicker label"
        )
        self.text_label = Label(
            self.driver,
            self.TEXT_LABEL,
            description="Handlers page -> New window"
        )

    def click_here(self):
        self.clicker_label.click()

    def get_text(self):
        self.driver.switch_active_window()
        return self.text_label.get_text()
