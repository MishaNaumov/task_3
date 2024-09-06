from pages.base_page import BasePage
from elements.webelement import WebElement
from elements.label import Label
import selenium.common


class AlertsContextPage(BasePage):
    UNIQUE_LOC = "//*[@id='content']//h3"
    TITLE_LOC = "//*[@id='content']//h3"
    FIELD_LOC = "//*[@id='hot-spot']"

    def __init__(self, driver):
        super().__init__(driver)

        self.field_web_element = WebElement(
            self.driver, self.FIELD_LOC,
            description="Alert + Context page -> "
                        "Alert + Context page web element")
        self.title_label = Label(self.driver, self.TITLE_LOC,
            description="Alert + Context page -> "
                        "Alert + Context page title")

    def click_field(self):
        self.field_web_element.right_click()

    def is_alert_closed(self):
        try:
            self.title_label.click()
            return True
        except selenium.common.TimeoutException:
            return False

