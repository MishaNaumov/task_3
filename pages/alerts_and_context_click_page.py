from pages.base_page import BasePage
from elements.webelement import WebElement
from elements.label import Label
import selenium.common


class AlertsContextPage(BasePage):
    UNIQUE_LOC = "//*[@id='content']//h3"

    TITLE_LABEL_LOC = "//*[@id='content']//h3"
    FIELD_WEB_ELEMENT_LOC = "hot-spot"

    def __init__(self, driver):
        super().__init__(driver)

        self.unique_element = Label(
            self.driver,
            self.UNIQUE_LOC,
            description="Alert + Context page -> Alert + Context page title"
        )

        self.field_web_element = WebElement(
            self.driver,
            self.FIELD_WEB_ELEMENT_LOC,
            description="Alert + Context page -> "
                        "Alert + Context page web element"
        )
        self.title_label = Label(
            self.driver,
            self.TITLE_LABEL_LOC,
            description="Alert + Context page -> Alert + Context page title"
        )

    def right_click_field(self):
        self.field_web_element.right_click()
