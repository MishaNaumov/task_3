from pages.base_page import BasePage
from elements.label import Label


class InfinityScrollPage(BasePage):
    UNIQUE_LOC = "//*[@id='content']//h3"

    PARAGRAPH_LABEL_LOC = "//div[@class='jscroll-added']{}"

    def __init__(self, driver):
        super().__init__(driver)

        self.unique_element = Label(self.driver, self.UNIQUE_LOC,
                                   description="Infinite Scroll page"
                                               " -> Infinite Scroll label")

        self.paragraph_label = Label(self.driver, self.PARAGRAPH_LABEL_LOC,
                                    description="Infinite Scroll page"
                                                " -> Paragraph label")
