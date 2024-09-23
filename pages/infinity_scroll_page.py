import time
from bs4 import BeautifulSoup
import requests


from pages.base_page import BasePage
from elements.label import Label
import selenium.common


class InfinityScrollPage(BasePage):
    UNIQUE_LOC = "//*[@id='content']//h3"

    PARAGRAPH_LABEL_LOC = "//div[@class='jscroll-added'][last()]"
    PARAGRAPH_23_LABEL_LOC = "//div[@class='jscroll-added'][23]"

    def __init__(self, driver):
        super().__init__(driver)

        self.unique_element = Label(self.driver, self.UNIQUE_LOC,
                                   description="Infinite Scroll page"
                                               " -> Infinite Scroll label")

        self.paragraph_label = Label(self.driver, self.PARAGRAPH_LABEL_LOC,
                                    description="Infinite Scroll page"
                                                " -> Paragraph label")
        self.paragraph_23_label = Label(self.driver, self.PARAGRAPH_23_LABEL_LOC,
                                     description="Infinite Scroll page"
                                                 " -> Paragraph label")

    def scroll(self):
        while True:
            self.driver.scroll_down(self.paragraph_label.presence_wait())
            src = self.driver.get_layout()
            soup = BeautifulSoup(src, "html.parser")
            if len(soup.find_all(class_="jscroll-added")) == 23:
                break
        return len(soup.find_all(class_="jscroll-added"))


